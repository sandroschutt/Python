#7)Escreva um programa que gere uma lista que é resultado do produto de duas listas L1 e
#L2. Mostre na tela as 3 listas.

lUm=[]
lDois=[]

for i in range(3):
    lUm.append(int(input('Insira um número na lista 1: ')))
    lDois.append(int(input('Insira um número na lista 2:')))

listaFinal=[]
for i in range(3):
    listaFinal.append(lUm[i]*lDois[i])

print('Lista A: ', lUm, '\nLista B: ', lDois, '\nLista Final: ', listaFinal)

