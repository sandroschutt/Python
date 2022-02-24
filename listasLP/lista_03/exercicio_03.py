#Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1a coluna da
#matriz são armazenados os nomes dos vendedores, da 2a coluna a 4a coluna dão
#armazenados as total de vendas por mês de cada vendedor, portando na 2a
#coluna é armazenado a venda do mês 1, 3a coluna do mês 2 e na 4a coluna do
#mês 3. Calcule e mostre na tela:
#a) O valor total vendido por vendedor
#b) A maior venda do mês 1
#c) A menor venda do mês 3
#d) O total vendido por mês

matrizPrincipal = [['Sandro',500.0,750.0,300.0],['Ana',600.0,400.0,450.0],['Paulo',200.0,300.0,900.0],['Beatriz',700.0,600.0,800.0],['Rafael',200.0,300.0,400.0]]
totalVendasIndividuais = []

def valorTotalPorVendedor (matrizPrincipal, totalVendasIndividuais):
    for i in matrizPrincipal:
        totalPorVendedor = 0
        for j in i:
            if isinstance(j, float):
                totalPorVendedor += j
        
        totalVendasIndividuais.append(totalPorVendedor)

    print('Total de vendas por vendedor:',
        '\nVendedor: ', matrizPrincipal[0][0], ' Total de vendas:', totalVendasIndividuais[0],
        '\nVendedor: ', matrizPrincipal[1][0], ' Total de vendas:', totalVendasIndividuais[1],
        '\nVendedor: ', matrizPrincipal[2][0], ' Total de vendas:', totalVendasIndividuais[2],
        '\nVendedor: ', matrizPrincipal[3][0], ' Total de vendas:', totalVendasIndividuais[3],
        '\nVendedor: ', matrizPrincipal[4][0], ' Total de vendas:', totalVendasIndividuais[4],)

def maiorVendaMesUm(matrizPrincipal):
    maiorVenda = 0
    for i in matrizPrincipal:
        if maiorVenda < i[1]:
            maiorVenda = i[1]

    print('Maior venda do 1º mês: ', maiorVenda)


def menorVendaMesTres(matrizPrincipal):
    menorVenda = 1000
    for i in matrizPrincipal:
        if menorVenda > i[3]:
            menorVenda = i[3]

    print('Menor venda do 3º mês: ', menorVenda)

def totalVendasPeriodo(matrizPrincipal):
    totalVendas = 0    
    for i in matrizPrincipal:
        for j in i:
            if isinstance(j, float):
                totalVendas += j
    
    print('Total vendido no período: ', totalVendas)
    
        
valorTotalPorVendedor(matrizPrincipal, totalVendasIndividuais)
maiorVendaMesUm(matrizPrincipal)
menorVendaMesTres(matrizPrincipal)
totalVendasPeriodo(matrizPrincipal)


                
