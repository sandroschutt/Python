#Escreva um programa que armazene em uma matriz, o nome e duas notas de 5
#alunos. Calcule e armazene em uma lista a média de cada aluno e em outra lista o
#status (media >= 6, “aprovado”, caso contrário, “reprovado”)
#• faça uma opção para que o usuário possa fazer uma pesquisar por nome. Se
#encontrar seja exibido na tela:
#o posição em que foi encontrado (índice);
#o nome do aluno;
#o as duas notas e a média;
#o status;

matrizPrincipal = [['Sandro','Maria','Vinicius','Alzira','Angela'],[4.5,5.0,6.5,7.0,8.5],[9.5,6.5,7.5,4.5,5.5]]
listaMedia = []
statusAlunos = []

for i in range(1, 2):
    for j in range(5):
        notaUm = matrizPrincipal[1][j]
        notaDois = matrizPrincipal[2][j] + notaUm
        mediaAlunos = notaDois / 2
        listaMedia.append(mediaAlunos)

        if mediaAlunos >= 6:
            status = 'aprovado'
        else:
            status = 'reprovado'

        statusAlunos.append(status)

pesquisa = str(input('Busque por um aluno no registro: '))

for i in matrizPrincipal[0]:
    if pesquisa == i:
        posicaoIndice = matrizPrincipal[0].index(i)
        print('Aluno: ',i,' Posição: ',posicaoIndice)
        print('1ª nota: ', matrizPrincipal[1][posicaoIndice],
            '\n2ª nota: ', matrizPrincipal[2][posicaoIndice],
            '\nMédia: ', listaMedia[posicaoIndice],
            '\nStatus: ', statusAlunos[posicaoIndice])

    if pesquisa not in matrizPrincipal[0]:
        print('Aluno não encontrado.')
        break
