# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4 
# 1  5  9
# 6  7  2

# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

from random import randint

def quadradoMagico(quadrado):
    somalinhas = []
    for i in quadrado:
        somalinhas.append(sum(i))

    colunas = [[],[],[]]
    for i in range(3):
        for j in range(3):
            colunas[i].append(quadrado[j][i])

    somaColunas = []
    for i in colunas:
        somaColunas.append(sum(i))

    contador = 0
    diagonais =[[],[]]
    for i in quadrado:
        diagonais[0].append(i[contador])
        contador+=1

    contador = 2
    for i in quadrado:
        diagonais[1].append(i[contador])
        contador-=1

    if somalinhas[0] == somalinhas[1] and somalinhas[0] == somalinhas[2]:
        if somaColunas[0] == somaColunas[1] and somaColunas[0] == somaColunas[1]:
            if sum(diagonais[0]) == somalinhas[0] and sum(diagonais[1]) == somalinhas[0]:
                print('Quadrado:')
                for i in quadrado:
                    print(i)
                print('Esse quadrado é mágico!')
    else:
        print('Esse quadrado não é mágico.')

    #teste de estruturas
    # print(f'Q: {quadrado}\nSL:{somalinhas}\nC:{colunas}\nD1:{diagonais[0]}\nD2:{diagonais[1]}')

# quadrado = [[8,3,4],[1,5,9],[6,7,2]] #Qdd perfeito para testes

quadrado = []
for i in range(3):
    defineQuadrado = []
    for j in range(3):
        defineQuadrado.append(randint(1,9))
    quadrado.append(defineQuadrado)

print('\nQuadrado:')
for i in quadrado:
    print(i)
print()
quadradoMagico(quadrado)