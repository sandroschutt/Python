# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = str(input('Nome: ').upper())
nome =list(nome)
nome.reverse()
nomeInvertido = "".join(nome)
print(f'Nome invertido: {nomeInvertido}')

#Inversão com WHILE 
# inverteNome = []

# contador = len(nome) - 1
# while contador >= 0:
#     inverteNome.append(nome[contador])
#     contador-=1

# print("".join(inverteNome))