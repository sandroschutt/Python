# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import os
from random import randint

def craps(soma, ponto):
    if soma == 7 or soma == 11 and ponto != 7:
        print(f'Dados: [{soma}]\nParabéns, você é um jogador nato!')
        os._exit(0)
    elif soma == 2 or soma == 3 or soma == 12:
        print(f'Dados: [{soma}]\nCRAPS! Você perdeu...\nTente novamente.')
        os._exit(0)
    else:
        print(f'Dados: [{soma}]\nPonto!\n Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.')
        ponto = soma if ponto == 0 else ponto
        if soma == 7:
            print(f'Dados: [{soma}]\nJogue novamente.')
            os._exit(0)

gear = True
while gear == True:
    dadoUm = randint(1,6)
    print(f'1º dado: [{dadoUm}]')
    dadoDois = randint(1,6)
    print(f'2º dado: [{dadoDois}]')
    soma = dadoUm + dadoDois
    ponto = 0

    craps(soma, ponto)

    if ponto == soma:
        print(f'Dados: [{soma}]\nParabéns, você venceu!')

    continuar = str(input('Deseja jogar novamente? [S/n] ').upper())

    gear = False if continuar != 'S' else True