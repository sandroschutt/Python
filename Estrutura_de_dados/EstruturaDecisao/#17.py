# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

#ano bissexto = 4 em 4 anos || ultimo = 2020

ano = int(input('Informe um ano: '))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0:
    print(f'O ano informado ({ano}) é bissexto.')
else:
    print(f'O ano informado ({ano}) não é bissexto.')