#screva um programa que preencha uma matriz 4 x 3 com números inteiros, calcule e
#mostre na tela:
#a) A soma dos elementos que estão na 2a e 4a linha da matriz
#b) A soma dos números primos

matrizPrincipal=[[],[],[],[]]
numerosPrimos=[]

for i in range(4):
    for j in range(3):
        matrizPrincipal[i].append(int(input('Informe um número: ')))
        
for i in matrizPrincipal:
    for j in i:
        contadorPrimo = 0
        for k in range(2, j - 1):
            if j % k == 0:
                print('não é primo')
                contadorPrimo += 1
        if (contadorPrimo == 0):
            numerosPrimos.append(j)

print('Matriz original: ', matrizPrincipal,
    '\nNúmeros primos: ', numerosPrimos,
    '\nSoma dos elementos da 2ª e 4ª linhas: ', sum(matrizPrincipal[1]) + sum(matrizPrincipal[3]),
    '\nSoma dos nº primos: ', sum(numerosPrimos))
