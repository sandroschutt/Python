# Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

alunos = []
alunosAcimaDaMedia = 0

for i in range(10):
    idade = int(input('\nIdade: '))
    altura = float(input('Altura: '))
    alunos.append([idade, altura])

somaAltura = 0
for i in alunos:
    somaAltura += i[1]

mediaAltura = somaAltura / len(alunos)

for i in alunos:
    if i[0] > 13 and i[1] > mediaAltura:
        alunosAcimaDaMedia += 1

print(f'\nLISTA ALUNOS:\n{alunos}\n\nMédia de altura dos alunos: {mediaAltura}\n\nNº de alunos com mais de 13 anos com altura acima da média: {alunosAcimaDaMedia}')