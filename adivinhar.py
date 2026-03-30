import random
import time

def jogar():
   novo=str(input("Jogar novamente?(s/n) "))
   if novo== "s":
     modos1()
   elif novo== "n":
     exit()
   elif novo== "b":
     tentas=0
     while True:
       print("VITOR GAY") #troll
       time.sleep(0.5)
       tentas += 1
       if tentas == 13:
         exit()
   else:
      print("Responta invalida")
      exit()

def facil():
    t= 0
    m1= random.randint(1, 10)
    while True:
      numero=int(input("digite um numero: "))
      t += 1
      if numero > m1:
        print("MENOS")
      elif numero==m1:
        print("!!VOCÊ ACERTOU!!")
        jogar()
      elif t >= 6:
       print("Maximo de Tentativas")
       jogar()
      else:
        print("MAIS")
      print(f"tentativa: {t}")

def medio():
    ten=0
    m2= random.randint(1, 20)
    while True:
      numero=int(input("digite um numero: "))
      ten += 1
      if numero > m2:
        print("MENOS")
      elif numero==m2:
        print("!!VOCÊ ACERTOU!!")
        jogar()
      elif ten >= 6:
       print("Maximo de Tentativas")
       jogar()
      else:
        print("MAIS")
      print(f"tentativa: {ten}")

def dificil():
    tenta=0
    m3= random.randint(1, 150)
    while True:
      numero=int(input("digite um numero: "))
      tenta += 1
      if numero > m3:
        print("MENOS")
      elif numero==m3:
        print("!!VOCÊ ACERTOU!!")
        jogar()
      elif tenta >= 6:
       print("Maximo de Tentativas")
       jogar()
      else:
        print("MAIS")
      print(f"tentativa: {tenta}")

def modos1():
   opcoes = {
     1: "1:Facil 1-20",
     2: "2:Medio 1-50",
     3: "3:Dificil 1-150"
   }
   for modo in [1,2,3]:
     print(opcoes.get(modo))
   x=int(input("Escolha o modo de jogo(coloque o numero): "))
   modo =(x)
   if modo == 1:
     print("Modo facil selecionado.")
     facil()
   elif modo == 2:
     print("Modo medio selecionado.")
     medio()
   elif modo == 3:
     print("Modo dificil selecionado!!!")
     dificil()
   else:
     print("modo não selecionado")

modos1()