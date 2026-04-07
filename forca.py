import time
import random
import os
print("Você está jogando FORCA\n")
print("\n------------------\n")
time.sleep(1)


def boneco0():
   print("""
   
  \
   
   \
""")
def boneco1():
   print("""
   O
  \
   
   \
""")
def boneco2():
   print("""
   O
  /\
   
   \
""")
def boneco3():
   print("""
   O
  /|\
   
   \
""")
def boneco4():
   print("""
   O
  /|\\
   
   \
""")
def boneco5():
   print("""
   O
  /|\\
   |
   \
""")
def boneco6():
   print("""
   O
  /|\\
   |
  / \
""")
def boneco7():
   print("""
   X
  /|\\
   |
  / \\
""")


bonecos = [boneco0, boneco1, boneco2, boneco3, boneco4, boneco5, boneco6, boneco7]
arquivo = open("ppl.txt")
palavras = arquivo.read().splitlines()
palavra = random.choice(palavras)
def jogo():
   palavra = random.choice(palavras)
   letras_certas=[]
   usadas = []
   tentativa=0
   while True:
     os.system("cls" if os.name == "nt" else "clear")
     time.sleep(0.3)
     linha = ""
     for letras in palavra:
       if letras in letras_certas:
          linha += letras + " "
       else:
          linha += "_ "
     print(linha)
     print("\n")
     if tentativa < len(bonecos):
       bonecos[tentativa]()
     if tentativa==7:
       print("acabou suas tentativas")
       novo()
       break
     print("Letras usadas:", ", ".join(usadas))
     if all(l in letras_certas for l in palavra):
       print("Você ganhou!")
       novo()
       break
     letra = input("Fale uma letra: ").lower().strip()
     if letra == "9":
       print(palavra)
       time.sleep(1)
     if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas UMA letra válida")
        time.sleep(1.1)
        continue
     if letra in usadas:
       print("Você já tentou essa letra")
       time.sleep(1.1)
       continue
     usadas.append(letra)
     if letra in palavra:
       if letra not in letras_certas:
         letras_certas.append(letra)
     else:
       tentativa +=1
def novo():
   nova=str(input("Deseja jogar novamente?(n/s)"))
   if nova=="s":
     print("Recomeçando")
     time.sleep(0.5)
     jogo()
   elif nova=="n":
     print("Fechando jogo.")
     time.sleep(0.5)
     exit()
   else:
     print("Nem uma resposta\n")
     time.sleep(0.6)
     print("Fechando jogo.")
jogo()