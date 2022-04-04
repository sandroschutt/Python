#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# valor = str(input('Qual valor deseja sacar? '))
value = "256"
saqueMil = print(f'Valor do saque: {value}\n10 notas de 100.') if value == '1000' else value

splitValue = list(value)
splitValue.append('0')

cashList = [[int(splitValue[0])],[0],[0],[0],[0]] #cashList = [[R$100],[R$50],[R$10],[R$10],[R$5],[R$1]]

while int(splitValue[1]) >= 5:
    cashList[1][0] += 1
    newValue50 = int(splitValue[1]) - 5
    splitValue[1] = str(newValue50)

if int(splitValue[1]) <= 5:
    cashList[2][0] += int(splitValue[1])

while int(splitValue[2]) >= 5:
    cashList[3][0] += 1
    newValue05 = int(splitValue[2]) - 5
    splitValue[2] = str(newValue05)   

rest = int(int(splitValue[2]) + int(splitValue[3]))
cashList.insert(4, str(rest))

print(f'Valor do saque: {value}\n{cashList[0]} notas de R$100\n{cashList[1]} notas de R$50\n{cashList[2]} notas de R$10\n{cashList[3]} notas de R$5\n{cashList[4]} notas de R$1.')