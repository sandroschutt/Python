#programa que receba a idade, e conforme a faixa etária exiba a mensagem
#se é criança, adolescente, adulto ou idoso.
#}De 0 a 12 anos – criança
#}De 13 a 17 anos – adolescente
#}De 18 a 59  anos– adulto
#}De 60 anos em diante - idoso

idade = int(input('Informe a idade: '))
if idade <= 12:
    print("Criança.")
elif idade <= 17:
    print('Adolescente.')
elif idade <= 59:
    print('Adulto.')
elif idade >= 60:
    print('Idoso.')
else:
    print('Valor informado inválido.')
