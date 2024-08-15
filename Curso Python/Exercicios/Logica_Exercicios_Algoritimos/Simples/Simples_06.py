# 6) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

combustivel = 4.87

odometroInicial = 0
odometroFinal = 0
consumo = 0
valorCorridasTotal = 0

def novaCorrida():
    global valorCorridasTotal
    valorCorrida = float(input("Qual foi o valor da corrida? "))
    valorCorridasTotal = valorCorridasTotal + valorCorrida
    pass

def novoDia(): #considerado tanque cheio de combustível
    global odometroInicial
    global odometroFinal
    global consumo
    odometroInicial = float(input("Qual a 'Km' indicada? "))
    novaCorrida()
    A = str(input("Fará uma nova corrida (s/n)? "))
    while A == 's':
        novaCorrida()
        A = str(input("Fará uma nova corrida (s/n)? "))
    else:
        consumo = float(input("Quantos litros de combustível completou? "))
        odometroFinal = float(input("Qual a 'Km' indicada? "))
    pass

novoDia()

print("A média do consumo em Km/L foi: ", (odometroFinal - odometroInicial) / consumo)
print("e o lucro (líquido) do dia foi (real): ", valorCorridasTotal - (consumo * combustivel))
