# 4) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que a potência necessária é de 18 watts por metro quadrado.

PotenciaReal = float(input("Qual a potência da lâmpada existente, em watts? "))
Largura = float(input("Qual a largura do cômodo, em metros'? "))
Comprimento = float(input("Qual o comprimento do cômod, em metros? "))
PotenciaIdeal = 18

metroQuadrado = Largura * Comprimento
PotenciaNecessaria = metroQuadrado * PotenciaIdeal
numeroLampadas = PotenciaNecessaria / PotenciaReal

print("A quantidade de lâmpadas é igual a: ", numeroLampadas)
