import time

def bubble(lista):
  #inicia o timer
    start=time.time()
    
    quantidade = len(lista)
    print(len(lista))
    for numero in range(quantidade):
      for posicao in range(quantidade - 1):
          if lista[posicao] > lista[posicao+1]:
            lista[posicao], lista[posicao+1] = lista[posicao+1], lista[posicao]
  # para o timer
    print(f"tempo_de_resposta: {time.time() - start:.2f}s")
    
    print(lista)
numeros = list(map(int, input("Digite seus numeros separados por espaço: ").split()))
bubble(numeros)

