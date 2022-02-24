#Escreva um programa que leia uma matriz 6 x 10, some as colunas
#individualmente e acumule as somas na 7a linha da matriz. O programa deverá
#mostrar o resultado de cada coluna.

matrizPrincipal=[
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10],
[1,2,3,4,5,6,7,8,9,10]]

setimaLinha = []

colunas = [[],[],[],[],[],[],[],[],[],[]]

def separaColunas(matrizPrincipal, colunas):
    for i in range(10):
        for j in matrizPrincipal:
            colunas[i].append(j[i])

def somaColunas(colunas, setimaLinha):
    for i in colunas:
        setimaLinha.append(sum(i))

separaColunas(matrizPrincipal, colunas)
somaColunas(colunas, setimaLinha)

matrizPrincipal.append(setimaLinha)


for i in range(10):
    print('Soma da %.1dª coluna' % i, matrizPrincipal[6][i])
