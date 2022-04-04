# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

listaCarne = []

carne = str(input('Escolha uma carne (1 - Filé Duplo (R$4,90kg); 2 - Alcatra (R$5,90kg); 3 - Picanha (R$6,90kg)):'))
qtdCarne = float(input('Quantos quilos deseja comprar? '))

if carne == '1':
    carne = 'Filé Duplo'
    precoCarne = 4.9 if qtdCarne < 5 else 5.8
elif carne == '2':
    carne = 'Alcatra'
    precoCarne = 5.9 if qtdCarne < 5 else 6.8
elif carne == '3':
    precoCarne = 6.9 if qtdCarne < 5 else 7.8
    carne = 'Picanha'

listaCarne.append([carne, qtdCarne, precoCarne])

formaPagamento = str(input('Qual a forma de pagamento (1 - dinheiro; 2 - crédito Tabajara; 3 - crédito; 4 - débito)? '))

valorCompra = listaCarne[0][2] * listaCarne[0][1]

precoFinal = valorCompra - (valorCompra * .05) if formaPagamento == '2' else valorCompra

print(f'\n----------------------------------\nHIPER MERCADO TABAJARA\n----------------------------------\n                         Valor(R$)\n{listaCarne[0][0]}     {listaCarne[0][1]}kg        R${precoFinal: .2f}\n\n')