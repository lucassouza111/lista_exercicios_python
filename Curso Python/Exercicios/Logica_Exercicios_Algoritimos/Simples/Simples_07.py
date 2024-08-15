# 7) A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de seu carro para que ele possa percorrer um determinado número de voltas até o primeiro reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os abastecimentos é o mesmo.

Comp = float(input("Qual o comprimento da pista, em metros? "))
Voltas = int(input("Quantas voltas serão realizadas? "))
Abastec = int(input("Quantos abastecimentos deseja realizar? "))
Consumo = float(input("De quanto é o consumo de combustível do carro, em Km/L? "))

kmTotal = Comp / 1000 * Voltas
consumoTotal = kmTotal / Consumo
litros = consumoTotal / Abastec

print("Número mínimo de litros necessários para percorrer até o primeiro reabastecimento, é: ", litros)
