# escreva um programa que preencha uma lista cin os nomes de cinco vendedores,
# preencha também outra lista com total vendido por cada vendedor.
# Cada vendedor recebe 15% de comissão sobre as vendas. Faça os seguintes cálculos
# e mostre o resultado na tela (2pt):
# a. Uma listagem com o nome e valor de comissão de cada vendedor (vendas *0.15) (2pt) FEITO
# b. O total de comissão pago pela empresa (5 vendedores) (1pt) FEITO
# c. a média das vendas (bruto) (1pt) FEITO
# d. a quantidade de vendedores que venderam abaixo da média (2pts) FEITO
# e. O maior valor de comissão e o nome do vendedor que recebeu (2pts)

vendrs = []  # vendedores
total_vendas = []  # total vendido
comss = []  # lista destinada apenas para comissões
nc = []  # nome e valor de comissão
tc = []  # total de comissões pagas pela empresa
vam = []  # vendas abaixo da média
i = 0
# x=0
while i < 5:
    nvnd = str(input('Informe o nome do vendedor: '))
    vendas = float(input('Informe o montante total vendido por ele: '))
    com = vendas * 0.15  # calcula comissão
    vendrs.append(nvnd)
    total_vendas.append(vendas)
    nc.append(nvnd)
    nc.append(com)
    tc.append(com)
    comss.append(com)
    med = sum(total_vendas) / len(total_vendas)  # calcula média das vendas
    if vendas <= med:
        vam.append(vendas)
    if com == max(comss):
        mc = com
        mv = nvnd
    i += 1

print('Nome e valor da comissão dos vendedores: ', nc)
print('Total da comissão paga pela empresa: %.2f' % sum(tc))
print('Média das vendas brutas: %.2f' % med)
print('Quantidade de vendedores que ficaram abaixo da média de vendas: %d' % len(vam))
print('A maior comissão foi de R$', mc, 'do vendedor ', mv)
