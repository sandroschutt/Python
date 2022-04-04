# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def converteData(dia,mes,ano,seculo):
    listaMeses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    dia = dia if dia > 0 and dia <= 31 else int(input('Dia(DD): '))
    mes = mes if mes > 0 and mes <= 12 else int(input('Mês(MM): '))
    ano = ano if len(str(ano)) <= 2 and len(str(ano)) > 0 else int(input('Ano(AA): '))
    seculo = seculo if len(str(seculo)) <= 2 and len(str(seculo)) > 0 else int(input('Século(SS): '))

    print(f'{dia} de {listaMeses[mes-1]} de {seculo-1}{ano}')

dia = int(input('Dia(DD): '))
mes = int(input('Mês(MM): '))
ano = int(input('Ano(AA): '))
seculo = int(input('Século(SS): '))
converteData(dia,mes,ano,seculo)

