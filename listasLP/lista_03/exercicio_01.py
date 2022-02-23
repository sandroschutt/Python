#Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros,
#calcule e mostre na tela:
#a) menor número da matriz;
#b) soma dos números múltiplos de 3 da matriz;
#c) média dos números da matriz;

matrizNumeros = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
multiplosDeTres = []
mediaMatriz = []

for i in range(3):
    for j in range(5):
        if matrizNumeros[i][j] <= 1:
            menorNota = matrizNumeros[i][j]

for i in range(3):
    for j in range(5):
        if matrizNumeros[i][j] % 3 == 0:
            multiplosDeTres.append(matrizNumeros[i][j])

for i in range(3):
    mediaMatriz.append(sum(matrizNumeros[i]))

print('Menor nota: ', menorNota, '\nSoma dos múltiplos de 3: ', sum(multiplosDeTres), '\nMédia das notas da matriz: ', (sum(mediaMatriz) / 15))
