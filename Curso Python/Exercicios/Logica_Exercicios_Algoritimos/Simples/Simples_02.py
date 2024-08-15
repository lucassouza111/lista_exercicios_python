# 2) Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius. (C = (F-32) * 5 / 9)

F = float(input("Qual a temperatura, em F°? "))
C = 0

def Celso():
  global C
  C = (F - 32) * 5 / 9
  print("A temperatura em Celso, é ", C)

Celso()

print(C)