#5)Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com
#o valor dos produtos. Calcule e mostre:
#a. a quantidade de produtos que o valor é abaixo de 10 reais;
#b. a média dos valores dos produtos;
#c. a quantidade de produtos com valor acima da média;
#d. a maior valor e o nome do produto;
#e. faça uma listagem que imprima na tela (Nome Vlr do produto)

listaProdutos = []
ListaValores = []
NomeValorProduto = []
valoresAbaixoDez = []
pam = []

print('**REGISTRO DE PRODUTOS**')
print('Digite 0 nos dois campos para encerrar o registro.')

for i in range(5):
    NomeProduto = str(input('Nome do produto: '))
    listaProdutos.append(NomeProduto)
    NomeValorProduto.append(NomeProduto)
    valor=float(input('Valor: '))
    ListaValores.append(valor)
    NomeValorProduto.append(valor)
    if valor<10.0 and valor>0:
        valoresAbaixoDez.append(valor)
    if valor == max(ListaValores):
        mvalor = valor
        mproduto = produto

pamc = (sum(ListaValores)/len(ListaValores))

contador = len(ListaValores)
x = 0

while x < contador:
    if ListaValores[x] > pamc:
        prc = ListaValores[x]
        pam.append(prc)
    x+=1

print('Quantidade de produtos abaixo de R$10.0: ', len(valoresAbaixoDez))
print('Média de valor dos produtos: R$ %.2f' % pamc)
print('Quantidade de produtos com valor acima da média: ', len(pam))
print('O produto mais caro é ', mproduto,'no valor de R$', mvalor)
print('Nome e valor dos produtos: ', NomeValorProduto)
