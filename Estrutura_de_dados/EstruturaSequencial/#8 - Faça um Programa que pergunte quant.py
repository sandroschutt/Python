#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadasMes = int(input('Quantas horas você trabalha por mẽs? '))

salarioMensal = salarioHora * horasTrabalhadasMes

print(f'Trabalhando {horasTrabalhadasMes}h por mês, sendo que sua hora de trabalho vale R${salarioHora}, seu salário será R$%.2f' % salarioMensal)