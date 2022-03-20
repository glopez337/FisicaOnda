#Colocar os parâmetros de entrada pelo input do usuário
#Criar um menu
import os
import math
import time

def funcao_f():
  freq = float(input("Insira a frequência: "))
  c = 3 * pow(10, 8)/freq
  k = 2 * math.pi/c
  w = 2 * math.pi * freq
  print("Comprimento da onda (λ): {:.2e} m".format(c))
  print("Numero de ondas (k): {:.2e} rad/m".format(k))
  print("Frequência angular (w): {:.2e} rad/s".format(w))
  
def funcao_lamb():
  comp = float(input("Insira o comprimento da onda: "))
  f = 3 * pow(10, 8)/comp
  k = 2*math.pi/comp
  w = 2*math.pi*f
  print("Frequência: {:.2e} Hz".format(f))
  print("Numero de ondas: {:.2e} onda".format(k))
  print("Frequência angular: {:.2e} rad/s".format(w))
  
def funcao_k():
  numOnda = float(input("Insira o número de ondas: "))
  c = 2 * math.pi / numOnda
  f = 3 * pow(10, 8) / c
  w = 2 * math.pi * f
  print("Frequência (f): {:.2e} Hz".format(f))
  print("Comprimento da onda (λ): {:.2e} m".format(c))
  print("Frequência angular (w): {:.2e} rad/s".format(w))


def funcao_w():
  w = float(input("Insira a frequência angular: "))
  f = w/(2*math.pi)
  comp = 3 * pow(10, 8)/f
  k = (2*math.pi)/comp
  print("Frequência: {:.2e} Hz".format(f))
  print("Comprimento de onda: {:.2e} m".format(comp))
  print("Numero de ondas: {:.2e} onda".format(k))

def funcao_em():
  em = float(input("Insira a o valor da amplitude do campo magnético (Em): "))
  bm = em/ 3 * pow(10, 8)  
  print("Módulo máximo: {:.2e} Hz".format(bm))
  
def funcao_bm():
  bm = float(input("Insira a o valor do campo magnético máximo (Bm): "))
  em = bm * (3 * pow(10, 8))
  print("Amplitude do campo magnético: {:.2e} Hz".format(em))
    
  
def main():
  print(" ____________________________________")
  print("|         ENTRADA DE VALORES         |")
  print("|____________________________________|")
  print("|_________PARÂMETROS DA ONDA_________|")
  print("|____________________________________|")
  print("|Digite o parâmetro inicial:         |")
  print("|1. Frequência (f)                   |") 
  print("|2. Comprimento de onda (λ)          |")
  print("|3. Número de onda (k)               |")
  print("|4. Frequência angular (ω)           |")
  print("|5. Campo magnético máximo (Bm)      |")
  print("|6. Módulo máximo (Em)               |")
  print("|____________________________________|")

  op = int(input("Escolha uma das opções: "))
  
  if op == 1:
    funcao_f()
  elif op == 2:
    funcao_lamb()
  elif op == 3:
    funcao_k()
  elif op == 4:
    funcao_w()
  elif op == 5:
    funcao_bm()
  elif op == 6:
    funcao_em()
  else:
    print("Valor incorreto! Opções de 1 a 6")
    main()






while(True):
  print(" __________________________________")
  print("|     Centro Universitário FEI     |")
  print("|__________________________________|")
  print("|________PARÂMETROS DA ONDA________|")
  print("|__________________________________|")
  print("|       Gabriel L. | Juan L.       | ")
  print("|      Pedro B. | Henrique C.      | ")
  print("|__________________________________|")
  input("|    Aperte enter para iniciar...  |\n")
  main()


    


