#Exercício 4: Faça um programa que preencha duas listas com 10 elementos cada. Depois
#percorra essas duas listas e gere uma terceira com números que se repetem
#nas duas listas. Mostre as tres listas na tela

listaA = []
listaB = []
listaC = []

for i in range(10):
    valoresListaA = (input("Insira um nº na Lista A: ", ))
    listaA.append(valoresListaA)

    valoresListaB = (input("Insira um nº na Lista B: ", ))
    listaB.append(valoresListaB)

listaC = list(set(listaA).intersection(listaB))

print(listaA)
print(listaB)
print(listaC)
