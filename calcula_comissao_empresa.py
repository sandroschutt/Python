# escreva um programa que preencha uma lista cin os nomes de cinco vendedores,
# preencha também outra lista com total vendido por cada vendedor.
# Cada vendedor recebe 15% de comissão sobre as vendas. Faça os seguintes cálculos
# e mostre o resultado na tela (2pt):
# a. Uma listagem com o nome e valor de comissão de cada vendedor (vendas *0.15) (2pt)
# b. O total de comissão pago pela empresa (5 vendedores) (1pt)
# c. a média das vendas (bruto) (1pt)
# d. a quantidade de vendedores que venderam abaixo da média (2pts)
# e. O maior valor de comissão e o nome do vendedor que recebeu (2pts)

vendedores = []
totalVendas = []
listaComissoes = []  # lista destinada apenas para comissões
nomeValorComissao = []  # nome e valor de comissão
totalComissoes = []  # total de comissões pagas pela empresa
vendasAbaixoMedia = []  # vendas abaixo da média

for i in range(5):
    nomeVendedor = str(input('Informe o nome do vendedor: '))
    vendas = float(input('Informe o montante total vendido por ele: '))
    comissao = vendas * 0.15  # calcula comissão
    vendedores.append(nomeVendedor)
    totalVendas.append(vendas)
    nomeValorComissao.append(nomeVendedor)
    nomeValorComissao.append(comissao)
    totalComissoes.append(comissao)
    listaComissoes.append(comissao)
    media = sum(totalVendas) / len(totalVendas)  # calcula média das vendas
    if vendas <= media:
        vendasAbaixoMedia.append(vendas)
    if com == max(listaComissoes):
        maiorComissao = comissao
        melhorVendedor = nomeVendedor

print('Nome e valor da comissão dos vendedores: ', nomeValorComissao)
print('Total da comissão paga pela empresa: %.2f' % sum(totalComissoes))
print('Média das vendas brutas: %.2f' % media)
print('Quantidade de vendedores que ficaram abaixo da média de vendas: %d' % len(vendasAbaixoMedia))
print('A maior comissão foi de R$', maiorComissao, 'do vendedor ', melhorVendedor)
