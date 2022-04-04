# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))

for i in range(num1 + 1, num2):
    print(i)