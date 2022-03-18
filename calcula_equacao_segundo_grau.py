# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

#DELTA = b² – 4ac
#EQUAÇÃO = x = -b +-²/delta | 2 * a

import math
import os

a = float(input('Informe o valor de a: '))
if a == 0:
    print('Valor informado não é permitido em equações de segundo grau.')
    os._exit(0)
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('O delta calculado é negativo, a equação não possui raizes reais.')
    os._exit(0)
elif delta == 0:
    raizUm = -b + (math.sqrt(delta)) / (2 * a)
    raizDois = -b - (math.sqrt(delta)) / (2 * a)
    print(f'1ª Raiz: {raizUm: .1f}\n2ª Raiz: {raizDois: .1f}')
elif delta > 0:
    raizUm = -b + (math.sqrt(delta)) / (2 * a)
    raizDois = -b - (math.sqrt(delta)) / (2 * a)
    print(f'1ª Raiz: {raizUm: .1f}\n2ª Raiz: {raizDois: .1f}')