#2) Faça um programa que preencha uma lista com 10 cores diferentes. Depois permita fazer
#uma pesquisa se uma determinada cor existe armazenada na lista, se existir deve ser
#impresso na tela a cor e em qual posição (índice) esta cor está armazenada. A pesquisa
#deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista.

listaCores=['vermelho','azul','amarelo','verde','roxo','branco','preto','laranja','bege','marrom']

print('Busque pelas cores na lista (digite FIM para encerrar)')

n=1
while n > 0:
    n = 1
    pesquisa = str(input('Busca de cores: '))
    if pesquisa in listaCores:
        print('A cor ', pesquisa, 'está presente na posição ',listaCores.index(pesquisa))
    if pesquisa == "FIM":
        n=0
    else:
        print('A cor informada não está na lista.')

print('O programa foi encerrado.')
