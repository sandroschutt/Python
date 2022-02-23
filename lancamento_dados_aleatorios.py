#faça um programa que simule um lançamento de dados. Lance o dado 10 vezes
#e armazene os resultados em uma lista. Depois, mostre quantas vezes o valor
#foi conseguido.
#um vetor de contadores (1-6) e uma função para gerar números aleatórios, simulando
#o lançamento dos dados.

from random import randint
lista=[0]*7
for i in range(20):
    n=randint(1,6)
    print('Número: ', n)
    lista[n]=lista[n]+1

for i in range(1,7):
    print('Número: ',i, 'qtde: ',lista[i])