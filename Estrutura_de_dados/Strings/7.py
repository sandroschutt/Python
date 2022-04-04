# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = str(input('Frase: '))
frase = list(frase)

vogais = [['a','e','i','o','u'],[0,0,0,0,0]]
brancos = 0

for i in frase:
    if i == " ":
        brancos+=1
    for j in vogais[0]:
        if i == j:
            indice = vogais[0].index(j)
            vogais[1][indice]+=1

print(f'Nº de espaços em branco na frase: {brancos}\nNº de vogais na frase:\nA:{vogais[1][0]}   E:{vogais[1][1]}   I:{vogais[1][2]}   O:{vogais[1][3]}   U:{vogais[1][4]}')