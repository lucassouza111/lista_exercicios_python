# 3) Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit. (F = (C × 9/5) + 32)

C = float(input("Qual a temperatura, em C°? "))
F = 0

def Fahrenheit():
  global F
  F = (C * 9 / 5) + 32
  print("A temperatura em Fahrenheit, é ", F)

Fahrenheit ()

print(F)