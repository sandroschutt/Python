#11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input('Informe o salário do funcionário (R$): '))

if salario <= 280:
    print(f'Salário sem reajuste: R${salario: .2f}\nPercentual de aumento: 20%\nValor do aumento: R${salario * .2}\nSalário reajustado: R${salario + (salario * .2): .2f}')
if salario > 280 and salario <= 700:
    print(f'Salário sem reajuste: R${salario: .2f}\nPercentual de aumento: 15%\nValor do aumento: R${salario * .15}\nSalário reajustado: R${salario + (salario * .15): .2f}')
if salario > 700 and salario <= 1500:
    print(f'Salário sem reajuste: R${salario: .2f}\nPercentual de aumento: 10%\nValor do aumento: R${salario * .1}\nSalário reajustado: R${salario + (salario * .1): .2f}')
if salario > 1500:
    print(f'Salário sem reajuste: R${salario: .2f}\nPercentual de aumento: 5%\nValor do aumento: R${salario * .05}\nSalário reajustado: R${salario + (salario * .05): .2f}')