# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

import os
from random import randint

# Importa palavras do arquivo 'listaPalavras.txt'
listaPalavras = []
arquivo = open('/home/sschutt/Documentos/pratica_python/Strings/9/listaPalavras.txt', 'r')

for i in arquivo:
    listaPalavras.append(i)

arquivo.close()

# sorteia uma palavra da lista
palavra = listaPalavras[randint(0,(len(listaPalavras)-1))]
palavra = list(palavra)
for i in palavra:
    if i == '\n':
        palavra.pop()

#Configura layout forca
# print(palavra)

erros = int(0)
charOculto = []
for i in range(0, (len(palavra))):
    charOculto.append('_ ')

charOcultoSaida = "".join(charOculto)
print(f'A palavra é: {charOcultoSaida}')

# separa a palavra para futura comparação
comparaPalavra = "".join(palavra)

#jogo
while erros < 6:
    tentativa = str(input('\nDigite uma letra: ').upper())
    if tentativa not in palavra:
        erros+=1
        print(f'A letra {tentativa} não está na palavra.\nVocê tem mais {6 - erros} chances.')
        if erros == 6:
            print('Você perdeu...')
            os._exit(0)
    else:
        for i in palavra:
            if tentativa == i:
                charOculto[palavra.index(i)] = tentativa
                palavra[palavra.index(i)] = ''
                charOcultoSaida = "".join(charOculto)
                print(f'\nVocê acertou uma letra!\nA palavra é: {charOcultoSaida}')
                if charOcultoSaida == comparaPalavra:
                    print('Você venceu!')
                    os._exit(0)
