#Escreva um programa que preencha uma listar com os nomes de 10 alunos, e
#outra lista com a média dos alunos. Calcule e mostre:
#a) a média da classe;
#b) a quantidade de alunos que tiveram média igual ou superior a 7;
#c) a quantidade de alunos que tiveram média abaixo de 7;
#d) a maior média da classe e nome do aluno que obteve a maior média

nomeAlunos = []
mediaAlunos = []

aprovados = 0
reprovados = 0

for i in range(10):
    nome = str(input('Informe o nome do aluno: '))
    media = float(input('Informe a média do aluno: '))
    nomeAlunos.append(nome)
    mediaAlunos.append(media)

    if media >= 7:
        aprovados += 1
    else:
        reprovados += 1

for i in mediaAlunos:
    if i == max(mediaAlunos):
        indice = mediaAlunos.index(i)


print('Média da classe: ',sum(mediaAlunos) / len(mediaAlunos),
'\nNº de notas superiores ou iguais a 7: ',aprovados,
'\nNº de notas abaixo de 7: ',reprovados,
'\nMaior media: ',max(mediaAlunos),' Aluno: ', nomeAlunos[indice])
