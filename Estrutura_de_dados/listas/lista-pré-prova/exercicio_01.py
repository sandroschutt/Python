#-----VARIÁVEIS-----

periodo = int((input("Informe o período (diurno(1)/noturno(2)): ")))
horasTrabalho = int(input("Informe a quantidade de horas trabalhadas no período: "))
miliLitroHora = (10 * 60) * 60

#-----FUNÇÕES-----

def producaoDia (horasTrabalho, miliLitroHora):
    avaliacao = 1
    while avaliacao == 1:
        if horasTrabalho <= 17 and horasTrabalho > 0:
            capacidadeGarrafa = 355
            producaoDia = miliLitroHora * horasTrabalho
            print("Nº de garrafas (355ml) produzidas no período diurno: %.2d" % (producaoDia / capacidadeGarrafa))
            avaliacao = 0
        else:
            horasTrabalho = int(input("Informe a quantidade de horas novamente: "))

def producaoNoite (horasTrabalho, miliLitroHora):
    avaliacao = 1
    while avaliacao == 1:
        if horasTrabalho <= 7 and horasTrabalho > 0:
            capacidadeGarrafa = 1000
            producaoNoite = miliLitroHora * horasTrabalho
            print("Nº de garrafas (1000ml) produzidas no período noturno: %.2d" % (producaoNoite / capacidadeGarrafa))
            avaliacao = 0
        else:
            horasTrabalho = int(input("Informe a quantidade de horas novamente: "))


#-----SAÍDA DE DADOS-----
producaoDia(horasTrabalho, miliLitroHora) if periodo == 1 else producaoNoite (horasTrabalho, miliLitroHora)
