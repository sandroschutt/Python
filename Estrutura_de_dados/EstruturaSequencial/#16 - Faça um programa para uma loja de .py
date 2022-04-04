#16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

areaPintura = int(input('Informe o tamanho da área a ser pintada (m²): '))
latasTintaNecessarias = areaPintura / (18 * 3)

print(f'Dimensão da área a ser pintada: {areaPintura}m²\nQuantidade de latas necessárias: %.2f ' % latasTintaNecessarias)

valorTotal = latasTintaNecessarias * 80
valorTotalReal = valorTotal if valorTotal >= 80 else 80

print('Valor total: R$%.2f' % valorTotalReal)

