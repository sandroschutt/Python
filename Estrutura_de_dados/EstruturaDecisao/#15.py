#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lados = []

for i in range(3):
    lado = float(input(f'Informe o {i+1}º lado do triângulo: '))
    lados.append(lado)

if lados[0] == lados[1] and lados[0] == lados[2]:
    print('Os lados informados formam um TRIÂNGULO.')
    print('TRIÂNGULO EQUILÁTERO.')
elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    print('Os lados informados formam um TRIÂNGULO.')
    print('TRIÂNGULO ISÓSCELES.')
elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
    print('Os lados informados formam um TRIÂNGULO.')
    print('TRIÂNGULO ESCALENO.')