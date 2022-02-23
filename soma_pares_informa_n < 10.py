#Faça um programa que recebe dez números,
#calcule e mostre na tela:
#a soma dos números pares
#a quantidade de números inferiores a 10

listaNumeros = [[], []]
x=0
while x<10:
    numeroInformado=int(input('Informe um número: '))
    if (numeroInformado % 2) == 0:
        listaNumeros[0].append(numeroInformado)
    if numeroInformado < 10:
        listaNumeros[1].append(numeroInformado)
    x+=1

print('Soma dos pares: ', sum(listaNumeros[0]))
print('Números menores que dez: ', listaNumeros[1])



