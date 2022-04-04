# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import os
from random import randint
import random

arquivo = open('/home/sschutt/Documentos/pratica_python/Strings/13/listaPalavras.txt', 'r')

listaPalavras = []
for i in arquivo:
    listaPalavras.append(i)

arquivo.close()

palavra = listaPalavras[randint(0,(len(listaPalavras)-1))]
palavra = list(palavra)

if '\n' in palavra:
    palavra.remove('\n')

palavraOriginal = "".join(palavra)
random.shuffle(palavra)

palavraEmbaralhada = "".join(palavra)

print(f'Que palavra é essa?\n{palavraEmbaralhada}')

erros = 0
while erros < 6:
    tentativa = str(input('\nAdivinhe a palavra: ').upper())
    if tentativa == palavraOriginal:
        print('Parabéns, você acertou!')
        os._exit(0)
    else:
        erros+=1
        progresso = print(f'Você errou. Você tem mais {6 - erros} chances.\n') if erros < 6 else print('Você perdeu...')