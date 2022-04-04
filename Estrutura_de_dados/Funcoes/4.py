# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def PositivoNegativo(numero):
    if numero >= 0:
        print(f'{numero}: P')
    else:
        print(f'{numero}: N')

numero = int(input('Nº: '))
PositivoNegativo(numero)