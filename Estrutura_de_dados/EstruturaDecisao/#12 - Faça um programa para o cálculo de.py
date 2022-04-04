#12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valorHora = float(input('Informe o valor da hora trabalhada: R$'))
horasTrabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))

salarioBruto = horasTrabalhadas * valorHora

if salarioBruto <= 900:
    print(f'Isento de descontos.\nSalário bruto: R${salarioBruto: .2f}\nSalário liquido: R${salarioBruto: .2f}')
elif salarioBruto > 900 and salarioBruto <= 1500:
    percentualIR = '5%'
    IR = salarioBruto * .05
    INSS = salarioBruto * .1
    FGTS = salarioBruto * .11
    totalDescontos = IR + INSS
    salarioLiquido = salarioBruto - totalDescontos
elif salarioBruto > 1500 and salarioBruto <= 2500:
    percentualIR = '10%'
    IR = salarioBruto * .1
    INSS = salarioBruto * .1
    FGTS = salarioBruto * .11
    totalDescontos = IR + INSS
    salarioLiquido = salarioBruto - totalDescontos
elif salarioBruto > 2500:
    percentualIR = '20%'
    IR = salarioBruto * .2
    INSS = salarioBruto * .1
    FGTS = salarioBruto * .11
    totalDescontos = IR + INSS
    salarioLiquido = salarioBruto - totalDescontos
else:
    print('Salário informado inválido.')

print(f'Salário bruto: R${salarioBruto: .2f}\n(-) IR ({percentualIR}): R${IR: .2f}\n(-) INSS ( 10%): R${INSS: .2f}\nFGTS (11%): {FGTS: .2f}\nTotal de descontos: R${totalDescontos: .2f}\nSalário liquido: R${salarioLiquido: .2f}')