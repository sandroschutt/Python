#5)Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com
#o valor dos produtos. Calcule e mostre:
#a. a quantidade de produtos que o valor é abaixo de 10 reais;
#b. a média dos valores dos produtos;
#c. a quantidade de produtos com valor acima da média;
#d. a maior valor e o nome do produto;
#e. faça uma listagem que imprima na tela (Nome Vlr do produto)

listaProdutos = []
listaValores = []
nomeValorProduto = []
valoresAbaixoDez = []
produtosAcimaMedia = []

print('**REGISTRO DE PRODUTOS**')
print('Digite 0 nos dois campos para encerrar o registro.')

for i in range(5):
    NomeProduto = str(input('Nome do produto: '))
    listaProdutos.append(NomeProduto)
    nomeValorProduto.append(NomeProduto)
    valor=float(input('Valor: '))
    listaValores.append(valor)
    nomeValorProduto.append(valor)
    if valor<10.0 and valor>0:
        valoresAbaixoDez.append(valor)
    if valor == max(listaValores):
        maiorValor = valor
        produtoMaisCaro = produto

x = 0
while x < len(listaValores):
    if listaValores[x] > mediaPrecos:
        produtosAcimaMedia.append(listaValores[x])
    x+=1

print('Quantidade de produtos abaixo de R$10.0: ', len(valoresAbaixoDez))
print('Média de valor dos produtos: R$ %.2f' % sum(listaValores) / len(listaValores))
print('Quantidade de produtos com valor acima da média: ', len(produtosAcimaMedia))
print('O produto mais caro é ', produtoMaisCaro,'no valor de R$', maiorValor)
print('Nome e valor dos produtos: ', nomeValorProduto)
