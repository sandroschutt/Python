#1)Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista.
#Calcule e mostre:
#a) a menor idade
#b) a média das idades
#c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
##d) a quantidade de pessoas com idade maior que a média

listaIdades = []
idadeEntreVinteTrinta = []
idadeMaiorQueMedia = []

for i in range(10):
    idade = float(input('Informe a idade: '))
    listaIdades.append(idade)
    if idade > 19 and idade < 31:
        idadeEntreVinteTrinta.append(idade)

mediaIdades = (sum(listaIdades) / len(listaIdades))

for i in range(10):
    if listaIdades[i] > mediaIdades:
        idadeMaiorQueMedia.append(listaIdades[i])

print('Menor idade: ', min(listaIdades))
print('Média das idades: ', (sum(listaIdades)/x))
print('Número de pessoas entre 20 e 30 anos: ', len(idadeEntreVinteTrinta))
print('Número de pessoas acima da média de idade: ', len(idadeMaiorQueMedia))
