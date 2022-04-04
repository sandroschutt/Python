#11 - Faça um Programa que peça 2 números inteiros e um número real. #Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

numeroUm = int(input('Informe o primeiro número: '))
numeroDois = int(input('Informe o segundo número: '))
numeroReal = float(input('Informe um número real: '))

calculoUm = (numeroUm * 2) * (numeroDois / 2)
calculoDois = (numeroUm * 3) + numeroReal
calculoTres = numeroReal ** 3

print(f'O produto do dobro do primeiro com metade do segundo: {calculoUm}\nA soma do triplo do primeiro com o terceiro: {calculoDois}\nO terceiro elevado ao cubo: %.2f' % calculoTres)