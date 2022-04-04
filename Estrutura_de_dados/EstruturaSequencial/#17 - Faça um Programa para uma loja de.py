#17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. #Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, #considere latas cheias.


areaPintura = int(input('Informe o tamanho da área a ser pintada (m²): '))
latasTinta = areaPintura / (18 * 6)
galoesTinta = areaPintura / (3.6 * 6)

print(f'Dimensão da área a ser pintada: {areaPintura}m²\nQuantidade de latas necessárias: {latasTinta: .1f}\nQuantidade de galões necessários: {galoesTinta: .1f} ')

valorTotalLatas = (latasTinta + (latasTinta * .1)) * 80
valorTotalRealLatas = round(valorTotalLatas) if valorTotalLatas >= 80 else 80

valorTotalGaloes = (galoesTinta + (galoesTinta * .1)) * 25
valorTotalRealGaloes = round(valorTotalGaloes) if valorTotalGaloes >= 25 else 25

print('Valor total em latas(18L): R$%.2f' % valorTotalRealLatas)
print('Valor total em Galões(3.6L): R$%.2f' % valorTotalRealGaloes)