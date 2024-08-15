# 5) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5 m2.

Comprimento = float(input("Qual o comprimento do cômodo, em metros? "))
Largura = float(input("Qual a largura do cômodo, em metros? "))
Altura = float(input("Qual a altura do cômodo, em metros? "))
azulejosCaixa = 1.5 # m2

paredesMenor = (Largura * Altura) *2
paredesMaior = (Comprimento * Altura) *2
metroQuadrado = paredesMenor + paredesMaior
quantidadeCaixa = metroQuadrado / azulejosCaixa

print("A quantidade de caixas de azulejos, para se colocar em todas as suas paredes, são: ", float(quantidadeCaixa))
