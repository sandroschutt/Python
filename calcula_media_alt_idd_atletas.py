#Faça um programa que receba a idade e as
#alturas de 10 atletas.
#Calcule e mostre na tela:
#A maior idade
#A menor idade
#A média das alturas
#A maior altura

x = 0
listaAtletas = [[],[]]
while x < 10:
    idade = int(input('Informe a idade do atleta: '))
    altura = float(input('Informe a altura do atleta: '))
    listaAtletas[0].append(idade)
    listaAtletas[1].append(altura)
    x += 1

print('Maior idade: ', max(listaAtletas[0]))
print('Menor idade: ', min(listaAtletas[0]))
print('Média de altura: ', sum(listaAtletas[1]) / len(listaAtletas[1]))
print('Maior altura: ',  max(listaAtletas[1]))
