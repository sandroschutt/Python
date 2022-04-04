# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randint

def NumeroAleatorio():
    nAleatorio = randint(0,10)
    dados.append(nAleatorio)

dados = []
x = dados

for i in range(10):
    NumeroAleatorio()

for i in dados:
    contador = 0
    for j in x:
        if i == j:
            contador+=1
            
    print(f'Incidência de {i}: {contador}\n')

print(dados)