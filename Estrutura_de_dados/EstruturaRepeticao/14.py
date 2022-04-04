# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []
qtdPar = 0
qtdImpar = 0

for i in range(1, 11):
    num = int(input('Nº: '))
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        qtdPar += 1
    else:
        qtdImpar += 1

print(f'\nNúmeros informados:\n{numeros}\nPares: {qtdPar}\nÍmpares: {qtdImpar}')