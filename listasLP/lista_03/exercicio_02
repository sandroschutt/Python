#Escreva um programa que preencha uma matriz 4 x 6 com números inteiros,
#calcule e mostre na tela:
#a) A quantidade de números que estão no intervalo entre 10 e 30
#b) A soma dos números maiores que 10
#c) A soma dos números que estão na quarta coluna da matriz
#d) A média dos números da matriz que estão na terceira linha

matrizPrincipal = [[],[],[],[]]
intervaloDezTrinta = []
nMaioresQueDez = []
quartaColuna = []

def somaQuartaColuna (quartaColuna):
    for i in range(4):
        quartaColuna.append(matrizPrincipal[i][3])
    

for i in range(4):
    for j in range(6):
        numeroInformado = int(input('informe um número: '))
        matrizPrincipal[i].append(numeroInformado)
        if numeroInformado <= 29 and numeroInformado >= 11:
            intervaloDezTrinta.append(numeroInformado)
        if n > 10:
            nMaioresQueDez.append(numeroInformado)

print('Matriz: ', matrizPrincipal,
    '\nNúmeros no intervalo entre 10 e 30: ', intervaloDezTrinta,
    '\nNúmeros maiores que 10: ', nMaioresQueDez,
    '\nSoma dos nº na 4ª coluna: ', somaQuartaColuna(quartaColuna),
    '\nMédia dos números na 3ª linha: ', sum(matrizPrincipal[2]) / len(matrizPrincipal[2]))
