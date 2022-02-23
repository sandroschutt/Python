#3)Faça um programa que preencha duas listas, lista A e lista B com 5 números em cada.
#Gere a lista C, com os números da lista A e lista B. Depois calcule e mostre na tela a
#quantidade de números perfeitos. Um número é perfeito quando ele é igual a soma dos
#seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus
#divisores).

listaA = []
listaB = []
listaC = []
nunerosPerfeitos = []

for a in range(4):
    numeroA = int(input('Informe cinco números para a lista A: '))
    listaA.append(numeroA)
    listaC.append(numeroA)

for b in range(4):
    numeroB = int(input('Informe cinco números para a lista B: '))
    listaB.append(numeroB)
    listaC.append(numeroB)
    b += 1

for i in range(0,10):
    somaPerfeitos = 0
    d = 1
    for j in listaC[j]:
        if listaC[j] % j == 0:
            soma += j
            if soma == listaC[j]:
                nunerosPerfeitos.append(listaC[j])

print('Quantidade de números perfeitos: ', len(nunerosPerfeitos))
