# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def SomaImposto(taxaImposto, custo):
    custoFinal = custo+ (taxaImposto / 100 * (custo))
    print(f'\nPreço final: R${custoFinal: .2f}')

custo = float(input('Custo: R$'))
taxaImposto = int(input('Taxa(%): '))
SomaImposto(taxaImposto, custo)