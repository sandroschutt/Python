#exercício 18
#disponível em: https://wiki.python.org.br/ExerciciosListas

jogadores = []

def PercentualVotos(totalVotos, jogadores):
    for i in jogadores:
        percentual = (i[1] * 100) / totalVotos
        i.append(percentual)

for i in range(23):
    jogadores.append([i+1, 0])

print('Digite 0 para encerrar o programa.')

gearOne = True
while gearOne == 1:
    voto = int(input('\nInsira um voto: '))
    if voto > 0 and voto <= 23:
        for i in jogadores:
            if voto == i[0]:
                i[1] = i[1] + 1
    elif voto == 0:
        gearOne = False if voto == 0 else True
    else:
        print('Voto inválido. Tente novamente.')


totalVotos = 0
for i in jogadores:
    totalVotos = totalVotos + i[1] if i[1] != 0 else totalVotos

PercentualVotos(totalVotos, jogadores)

melhorJogador = [0,0]
for i in jogadores:
    if i[1] > melhorJogador[1]:
        melhorJogador = i

print(f'Enquete: Quem foi o melhor jogador?\n\n')

for i in jogadores:
    print(f'Camisa: {i[0]}  Votos: {i[1]}')

print(f'\n\nResultado da votação: \n\nTotal de votos computados: {totalVotos}\n\n')

for i in jogadores:
    if i[1] != 0:
        print(f'Camisa: {i[0]}  Votos: {i[1]}  Proporção: {i[2]: .2f}%\n\n')

print(f'O melhor jogador foi o nº {melhorJogador[0]}, com {melhorJogador[1]} votos, correspondendo a {melhorJogador[2]: .2f}% do total.')