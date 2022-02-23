#4) Escreva um programa que leia 10 notas e
#mostre na tela a média dos alunos e a quantidade
#de alunos que tiveram nota inferior a 6.

notas=[]
notasReprova=[]
x=0
while x<10:
    n=float(input('Informe a nota de um aluno: '))
    notas.append(n)
    x += 1
    if n<6:
        notasReprova.append(n)


print('Média da sala: ', sum(notas)/10)
print('Notas menores que seis: ', notasReprova)
