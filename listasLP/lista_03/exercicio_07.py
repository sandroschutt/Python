#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando
#dados sobre o salário, idade e o número de filhos. Escreva um programa que leia
#esses dados, por exemplo para 10 pessoas. Armazene esses dados em uma
#matriz, depois calcule e mostre:
#a) A média de salário da população
#b) A média do número de filhos
#c) A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
#d) A média de salário de pessoas que tem idade entre 20 a 30 anos

matrizPrincipal = [[],[],[]]

mediaSalarialEntreVinteTrinta = 0
filhosEntreQuinzeVinte = 0

for i in range(10):
    salario = float(input('Informe o salário: '))
    idade = int(input('informe a idade: '))
    filhos = int(input('Qtd de filhos: '))

    if idade > 14 and idade < 26 and filhos != 0:
        filhosEntreQuinzeVinte += 1

    if idade > 19 and idade < 31:
        mediaSalarialEntreVinteTrinta += salario

    matrizPrincipal[0].append(salario)
    matrizPrincipal[1].append(idade)
    matrizPrincipal[2].append(filhos)

print('Média salarial da população: ',sum(matrizPrincipal[0]) / len(matrizPrincipal[0]),
    '\nMédia de filhos: ',sum(matrizPrincipal[2]) / len(matrizPrincipal[2]),
    '\nQtd filhos de pessoas entre 15 e 25 anos: ', filhosEntreQuinzevinte,
    '\nMédia salarial (20 a 30 anos): ', mediaSalarialEntreVinteTrinta / 10)
