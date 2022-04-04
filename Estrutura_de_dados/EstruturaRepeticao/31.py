#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

import os

produtos = []

gear = True
while gear == True:
    valorProduto = float(input('Valor do produto: '))
    produtos.append(valorProduto)
    decisaoUsuario = str(input('Deseja inserir um novo valor? (s/n): '))
    gear = True if decisaoUsuario == 's' else False

valorTotal = sum(produtos)
print(f'Total a pagar: R${valorTotal}')
dinheiro = float(input('Quanto dinheiro foi fornecido pelo cliente? '))

if dinheiro < valorTotal:
    print('Dinheiro insuficiente para pagar a compra.')
    os.exit(0)
else:
    troco = dinheiro - valorTotal

print('\nLojas Tabajara')
for i in produtos:
    print(f'Produto {produtos.index(i) + 1}: R${i}')

print(f'Total: R${valorTotal}\nDinheiro: R${dinheiro}\nTroco: R${troco}')