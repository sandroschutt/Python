#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

import os


gear = True

while gear == True:
    num = int(input('Informe um nº para fatorar: '))
    numero = num if num > 0 and num <= 16 else os.exit()

    numPrint = num

    for i in range(1, num):
        num *= i

    print(f'\n{numPrint}! = {num}\n')
    continuar = str(input('Deseja fatorar outro número (s/n)? '))
    gear = True if continuar == 's' else False