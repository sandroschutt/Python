#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

caracteres = ['a','b','c','d','e','f','g','h','i','j']
vogais = ['a','e','i','o','u']

for i in caracteres:
    if i in vogais:
        caracteres.remove(i)

print(f'Nº de consoantes: {len(caracteres)}\n{caracteres}')