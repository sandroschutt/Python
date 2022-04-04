# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

classificacao = 0

telefonouPara = str(input('Telefonou para a vítima (s/n)? '))
classificacao += 1 if telefonouPara == 's' else 0

esteveNoLocal = str(input('Esteve no local do crime (s/n)? '))
classificacao += 1 if esteveNoLocal == 's' else 0

moraPerto = str(input('Mora perto da vítima (s/n)? '))
classificacao += 1 if moraPerto == 's' else 0

deviaPara = str(input('Devia para a vítima (s/n)? '))
classificacao += 1 if deviaPara == 's' else 0

trabalhouCom = str(input('Já trabalhou com a vítima (s/n)? '))
classificacao += 1 if trabalhouCom == 's' else 0

if classificacao == 2:
    print('Suspeito')
elif classificacao == 3 or classificacao == 4:
    print('Cúmplice')
elif classificacao == 5:
    print('Assassino')
else:
    print('Inocente')