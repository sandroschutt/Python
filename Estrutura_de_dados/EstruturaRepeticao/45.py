# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = ['A','B','C','D','E','E','D','C','B','A']
notasTurma = []
notaAluno = 0

def Avaliacao(gabarito, notaAluno, notasTurma):
    for i in gabarito:
        questao = str(input(f'Resposta questão {(gabarito.index(i)) + 1}: ').upper())
        if questao == i:
            notaAluno = notaAluno + 1
    notasTurma.append(notaAluno)
    
gear = True
while gear == True:
    notaAluno = 0
    Avaliacao(gabarito, notaAluno, notasTurma)

    continuar = str(input('Deseja avaliar mais um aluno (s/n)? '))
    gear = False if continuar == 'n' else True

print(f'\nMaior nota: {max(notasTurma)}\nMenor nota: {min(notasTurma)}\nTotal de alunos que utilizaram o sistema: {len(notasTurma)}\nMédia das notas da turma: {sum(notasTurma) / len(notasTurma)}')

print('\nGABARITO:')
for i in gabarito:
    print(f'Questão {gabarito.index(i)+1}: {i}')