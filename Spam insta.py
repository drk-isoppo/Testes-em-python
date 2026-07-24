from playwright.sync_api import Playwright, sync_playwright
import random
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir="perfil_instagram",
        headless=False
    )

    page = browser.new_page()

    page.goto("https://www.instagram.com/p/DbJN2ckx_6w/")
    time.sleep(2)

    contador = 0
    tempo_inicio = time.time()

    try:
        while True:

            tempo = random.randint(2, 5)

            with open("frases.txt", "r", encoding="utf-8") as arquivo:
                frases = arquivo.readlines()

            frases = [frase.strip() for frase in frases if frase.strip()]

            frase_escolhida = random.choice(frases)

            caixa_comentario = page.get_by_role(
                "textbox",
                name="Adicione um comentário..."
            )

            caixa_comentario.click()

            caixa_comentario.fill(frase_escolhida)

            page.get_by_role(
                "button",
                name="Postar",
                exact=True
            ).click()

            contador += 1

            tempo_passado = int(time.time() - tempo_inicio)

            print(f"Executou: {contador} vezes | Rodando há {tempo_passado} segundos")

            time.sleep(tempo)

            if time.time() - tempo_inicio >= 300:
                pausa = random.randint(15, 20)

                print(f"\nPausa iniciada por {pausa} segundos...")

                time.sleep(pausa)

                tempo_inicio = time.time()

                print("Voltando a executar...\n")

    except KeyboardInterrupt:
        print("\nPrograma parado pelo usuário.")
        print(f"Total de execuções: {contador}")

    browser.close()


with sync_playwright() as playwright:
    run(playwright)