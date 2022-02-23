i = 0
qtdMasculino = 0
qtdFeminino = 0
qtdCriançasDoisAnos = 0
qtdCriancas = int(input('Informe quantidade de crianças no período: '))
while i < qtdCriancas:
    sexo = str(input('Informe o sexo da criança (M - masculino; F - feminino;'))
    if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':
        if sexo == 'M' or sexo == 'm':
            qtdMasculino = qtdMasculino + 1
        else:
            qtdFeminino = qtdFeminino + 1
        idade = int(input('Informe quantos meses a criança viveu: '))
        if idade <= 24:
            qtdCriançasDoisAnos = qtdCriançasDoisAnos + 1
        i = i + 1
    else:
        print('Valor inválido. Insira um valor válido para continuar.')
        
mediaMasculino = (qtdMasculino/qtdCriancas)*100
mediaFeminino = (qtdFeminino/qtdCriancas)*100
mdPeriodo = (qtdCriançasDoisAnos/qtdCriancas)*100

print('Porcentagem de óbitos masculinos: ', mediaMasculino)
print('Porcentagem de óbitos femininos: ', mediaFeminino)
print('Porccentagem de óbitos de até 24 meses: ', mdPeriodo)
