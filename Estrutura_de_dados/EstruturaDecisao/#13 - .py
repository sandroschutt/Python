#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

entradaUsuario = int(input('Informe um dia da semana (1 - Domingo, 2 - Segunda...): '))
diasSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

for i in range(6):
    if diasSemana[entradaUsuario - 1] in diasSemana:
        print(f'Dia selecionado: {diasSemana[entradaUsuario - 1]}')
        break