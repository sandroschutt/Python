# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def Soma(n1,n2,n3):
    soma = n1 + n2 +n3
    print(f'Soma: {soma}')

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

Soma(n1,n2,n3)