#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

converteParaCelcius = 5 * ((fahrenheit - 32) / 9)

print(f'{fahrenheit}F equivalem a %.2f' % converteParaCelcius)

