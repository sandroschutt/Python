#Calcula aluno aprovado/reprovado
#requisito: usando apenas while e if

z = 1
while z > 0:
    nomeAluno = str(input('Informe o nome do aluno: '))
    x = 1
    while x > 0:
        provaUm = float(input('Informe a nota da p1: '))
        if provaUm >= 0 and provaUm <= 10:
            x = 0
        else:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            x = 1

    x = 1
    while x > 0:
        notaProjeto = float(input('Informe a nota do projeto: '))
        if notaProjeto >= 0 and notaProjeto <= 10:
            x = 0
        elif notaProjeto > 10:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            x = 1

    x = 1
    while x >= 1:
        notaListas = float(input('Informe a pontuação das listas: '))
        if notaListas <= 4 and notaListas >= 0:
            x = 0
        else:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            x = 1

    media = (provaUm * 0.2) + (notaProjeto * 0.4) + notaListas
    if media >= 6 and media <= 10:
        print('O aluno', nomeAluno, ' ficou com média', media, ' e foi aprovado.')
        restart = str(input('Deseja executar o programa novamente? (s/n)'))
        if restart == 's':
            z = 1
        else:
            z = 0

    elif media < 6:
        x = 1
        while x > 0:
            sub = float(input('Informe a nota da prova substitutiva: '))
            if sub >= 0 and sub <= 10:
                media = (sub * 0.2) + (nota_pro * 0.4) + listas
                x = 0
            elif sub < 6 and sub >= 0:
                media = (sub * 0.2) + (nota_pro * 0.4) + listas
                x = 0
            else:
                print('A nota informada está fora dos parâmetros. Informe novamente')
                x = 1
        if media >= 6 and media <= 10:
            print('O aluno', nomeAluno, ' ficou com média', media, ' e foi aprovado.')
            restart = str(input('Deseja executar o programa novamente? (s/n)'))
            if restart == 's':
                z = 1
            else:
                z = 0
        elif media < 6 and media >= 0:
            print('O aluno ', nomeAluno, 'teve média', media, 'e foi reprovado.')
            restart = str(input('Deseja executar o programa novamente? (s/n)'))
            if restart == 's':
                z = 1
            else:
                z = 0
