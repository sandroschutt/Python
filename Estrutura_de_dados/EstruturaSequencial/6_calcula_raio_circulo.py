#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²);

import math

raioCirculo = float(input('Informe o raio do circulo: '))

area = math.pi * (raioCirculo ** 2)

print(f'Um círcuo com raio de {raioCirculo} possui uma área de %.2f' % area)