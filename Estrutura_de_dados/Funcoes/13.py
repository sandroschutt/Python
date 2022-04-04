# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

import os

def retangulo(linhas, colunas):
    if linhas <= 0:
        linhas = 1
    elif linhas > 20:
        linhas = 20
    if linhas <= 0:
        linhas = 1
    elif linhas > 20:
        linhas = 20

    espaco = ' ' * (colunas-4)

    print('+',('-' * (colunas-4)),'+')
    for i in range(linhas):
        print('|', espaco, '|')
    print('+',('-' * (colunas-4)),'+')

linhas = int(input('Linhas: '))
colunas = int(input('Colunas: '))
retangulo(linhas, colunas)