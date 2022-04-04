# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

quantidadeLitros = int(input('Informe a quantidade de litros que deseja colocar no tanque: '))
tipoCombustivel = int(input('Qual combustível deseja utilizar (1 - Gasolina, 2 - Alcool): '))
quantidadeLitros = int(input('Informe a quantidade de litros que deseja colocar no tanue: '))
tipoCombustivel = int(input('Qual combustível deseja utilizar (1 - Gasolina, 2 - Alcool): ')

if tipoCombustivel == 1:
    precoGasolina = 2.5
    if quantidadeLitros <= 20:
        precoGasolina -= precoGasolina * .04
    elif quantidadeLitros > 20:
        precoGasolina -= precoGasolina * .06
    print(f'\nTOTAL A PAGAR (R$):\n{quantidadeLitros * precoGasolina}')

if tipoCombustivel == 2:
    precoAlcool = 1.9
    if quantidadeLitros <= 20:
        precoAlcool -= precoAlcool * .03
    elif quantidadeLitros > 20:
        precoAlcool -= precoAlcool * .05
    print(f'\nTOTAL A PAGAR (R$):\n{quantidadeLitros * precoAlcool}')

print('\nPROGRAMA ENCERRADO.')
if tipoCombustivel == 1:
    precoGasolina = 2.5
    if quantidadeLitros <= 20:
        precoGasolina -= precoGasolina * .04
    elif quantidadeLitros > 20:
        precoGasolina -= precoGasolina * .06
    print(f'\nTOTAL A PAGAR (R$):\n{quantidadeLitros * precoGasolina}')

if tipoCombustivel == 2:
    precoAlcool = 1.9
    if quantidadeLitros <= 20:
        precoAlcool -= precoAlcool * .03
    elif quantidadeLitros > 20:
        precoAlcool -= precoAlcool * .05
    print(f'\nTOTAL A PAGAR (R$):\n{quantidadeLitros * precoAlcool}')

print('\nPROGRAMA ENCERRADO.')