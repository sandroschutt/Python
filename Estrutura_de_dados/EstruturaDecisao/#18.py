#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Informe uma data (dd/mm/aaaa)'.upper())
dia = int(input('Informe um dia (dd): '))
mes = int(input('Informe um dia (mm): '))
ano = int(input('Informe um dia (aaaa): '))

if dia >= 1 and dia <= 31:
    if mes >=1 and mes <= 12:
        print(f'{dia}/{mes}/{ano}')
    else:
        print('Mês informado inválido.')
else:
    print('Dia informado inválido.')
