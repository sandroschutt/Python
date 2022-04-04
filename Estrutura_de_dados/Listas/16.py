#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante

# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

intervalos = [[200,299,0],[300,399,0],[400,499,0],[500,599,0],[600,699,0],[700,799,0],[800,8999,0],[900,999,0],[1000,0]]

gear = True
while gear == True:
    vendas = float(input('Bruto das vendas semanais: '))
    bonus = vendas * .09
    salario = 200 + bonus
    for i in intervalos:
        if salario in range(i[0],i[1]):
            i[2] += 1
    
    continuar = str(input('Deseja continuar (s/n)? '))
    gear = False if continuar == 'n' else True

print(f'\nQtd salarios entre $200 - $299: {intervalos[0][2]}\nQtd salarios entre $300 - $399: {intervalos[1][2]}\nQtd salarios entre $400 - $499: {intervalos[2][2]}\nQtd salarios entre $500 - $599: {intervalos[3][2]}\nQtd salarios entre $600 - $699: {intervalos[4][2]}\nQtd salarios entre $700 - $799: {intervalos[5][2]}\nQtd salarios entre $800 - $899: {intervalos[6][2]}\nQtd salarios entre $900 - $999: {intervalos[7][2]}\nQtd salarios acima de $1000: {intervalos[8][1]}\n')