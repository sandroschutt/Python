#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Informe um nº para fatorar: '))
numPrint = num

for i in range(1, num):
    num *= i

print(f'{numPrint}! = {num}')