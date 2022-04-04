# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtdMorangos = int(input('Quantidade de morangos (kg): '))
qtdMacas = int(input('Quantidade de maçãs (kg): '))

precoMorangos = 2.2 if qtdMorangos > 5 else 2.5
precoMacas = 1.5 if qtdMacas > 5 else 1.8

valorTotalMorangos = qtdMorangos * precoMorangos
valorTotalMacas = qtdMacas * precoMacas

valorTotal = valorTotalMorangos + valorTotalMacas
precoFinal = valorTotal - (valorTotal * .1) if valorTotal >= 25 else valorTotal

print(f'{qtdMorangos}kg de morango foram adquiridos por R${valorTotalMorangos: .2f}.\n{qtdMacas}kg de maçã foram adquiridos pelo cliente por R${valorTotalMacas: .2f}.\nValor da compra: R${precoFinal: .2f}.')