#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

notaUm = float(input('Informe a 1ª nota parcial: '))
notaDois = float(input('Informe a 2ª nota parcial: '))

media = (notaUm + notaDois) / 2

if media > 8.9:
    print(f'\n1ª nota: {notaUm}\n2ª nota: {notaDois}\nMédia do aluno: {media: .1f}\nConceito: A\nAPROVADO.')
elif media > 7.4 and media <= 8.9:
    print(f'\n1ª nota: {notaUm}\n2ª nota: {notaDois}\nMédia do aluno: {media: .1f}\nConceito: B\nAPROVADO')
elif media > 5.9 and media <= 7.4:
    print(f'\n1ª nota: {notaUm}\n2ª nota: {notaDois}\nMédia do aluno: {media: .1f}\nConceito: C\nAPROVADO')
elif media > 3.9 and media <= 5.9:
    print(f'\n1ª nota: {notaUm}\n2ª nota: {notaDois}\nMédia do aluno: {media: .1f}\nConceito: D\nREPROVADO')
elif media < 4.0:
    print(f'\n1ª nota: {notaUm}\n2ª nota: {notaDois}\nMédia do aluno: {media: .1f}\nConceito: E\nREPROVADO')