#Calcular salário bruto e líquido de três funcionários

#-----VARIÁVEIS-----
funcionarios = []
contratacao = []
quantidadeHoras = []
valorHoras = []
salarioBruto = []
salarioLiquido = []


#-----FUNÇÕES-----

def preencheMatrizes (funcionarios, contratacao, quantidadeHoras, valorHoras):
    for i in range(3):
        nome = str(input("Informe o nome do funcionário %d: " % i))
        funcionarios.append(nome)
        contrato = str(input("Informe o regime contratual do funcionário %d (pf/pj/clt): " % i))
        contratacao.append(contrato)
        horas = int(input("Informe qtd/horas do funcionário %d: " % i))
        quantidadeHoras.append(horas)
        valor = float(input("Informe o valor/hora do funcionário %d: " % i))
        valorHoras.append(valor)

def calculaSalarioBruto (quantidadeHoras, valorHoras, salarioBruto):
    for i in range(2):
        valorBruto = quantidadeHoras[i] * valorHoras[i]
        salarioBruto.append(valorBruto)

def calculaSalarioLiquido (contratacao, salarioBruto, salarioLiquido):
    for i in range(3):
        if contratacao[i] == "pj":
            desconto = salarioBruto[i] - (salarioBruto[i] * .02)
            salarioLiquido.append(desconto)
        elif contratacao[i] == "pf":
            desconto = salarioBruto[i] - (salarioBruto[i] * .07)
            salarioLiquido.append(desconto)
        elif contratacao[i] == "clt":
            desconto = salarioBruto[i] - (salarioBruto[i] * .09)
            salarioLiquido.append(desconto)


#-----SAÍDA DE DADOS-----
x = 0
while x < 1:
    preencheMatrizes(funcionarios,contratacao,quantidadeHoras,valorHoras)
    calculaSalarioBruto(quantidadeHoras, valorHoras, salarioBruto)
    calculaSalarioLiquido(contratacao, salarioBruto, salarioLiquido)

    print("Funcionário: %s" % funcionarios[0], "Salário Bruto: R$ %.2f" % salarioBruto[0], "Salário líquido: R$ %.2f" % salarioLiquido[0],
        "\nFuncionário: %s" % funcionarios[1], "Salário Bruto: R$ %.2f" % salarioBruto[1], "Salário líquido: R$ %.2f" % salarioLiquido[1],
        "\nFuncionário: %s" % funcionarios[2], "Salário Bruto: R$ %.2f" % salarioBruto[2], "Salário líquido: R$ %.2f" % salarioLiquido[2])

    reset=str(input("Deseja executar o programa mais uma vez (s/n)?  "))
    if reset == "s":
        x = 1
