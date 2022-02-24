#Calcular média dos aluons usando funções


#-----FUNÇÕES---------

def calculaMedia(provaUm, notaProjeto, notaListas):
    return (provaUm * 0.2) + (notaProjeto * 0.4) + notaListas

def validaNotaUm(provaUm):
    contador = 1
    while contador > 0:
        if provaUm >= 0 and provaUm <= 10:
            contador = 0
        else:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            provaUm = float(input('Informe a nota da prova: '))

def validaNotaDois(notaProjeto):
    contador = 1
    while contador > 0:
        if notaProjeto >= 0 and notaProjeto <= 10:
            contador = 0
        else:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            notaProjeto = float(input('Informe a nota do projeto: '))

def validaLista(notaListas):
    contador = 1
    while contador > 0:
        if notaListas >= 0 and notaListas <= 4:
            contador = 0
        else:
            print('A nota informada está fora dos parâmetros. Informe novamente.')
            notaListas = float(input('Informe a nota das listas: '))

def validaMedia(media):
    if media >= 6 and media <= 10:
        print('O aluno', nomeAluno, ' ficou com média', media, ' e foi aprovado.')

    elif media < 6 and media >= 0:
        notaSubstitutiva = float(input('informe a nota da sub: '))
        substitutiva = notaSubstitutiva * 0.2
        notadois = notaProjeto * .4
        media = substitutiva + notaDois + notaListas

        if media >= 6 and media <= 10:
            print('O aluno', nomeAluno, ' ficou com média', media, ' e foi aprovado.')

        elif media < 6 and media >= 0:
            print('O aluno ', nomeAluno, 'teve média', media, 'e foi reprovado.')


#------ENTRADA DE DADOS--------
z = 1
while z > 0:
    nomeAluno = str(input('Informe o nome do aluno: '))
    provaUm = float(input('Informe a nota da prova: '))
    validaNotaUm(provaUm)
    notaProjeto = float(input('Informe a nota do projeto: '))
    validaNotaDois(notaProjeto)
    notaListas = float(input('Informe a nota da lista: '))
    validaLista(notaListas)


#--------MÉDIA--------------------
    media = float(calculaMedia(provaUm, notaProjeto, notaListas))
    validaMedia(media)


#--------RESET--------------------
    reset = str(input('Deseja reiniciar o programa (s/n): '))
    if reset == 'n':
        z=0
    else:
        z=1
