#Faça um programa que receba um número
#inteiro. Calculo o fatorial desse número e
#mostre na tela.

#O fatorial de um número inteiro e positivo “n”,
# representado por “n!” é obtido a partir da multiplicação de
# todos os seus antecessores até o número um, cuja
# expressão genérica é n! = n . (n – 1). (n – 2).

num=int(input('Insira um número: '))
fat=1
i=1
for i in range(1,num+1):
    fat=fat*i
    i+=1

print("O fatorial do número informado é: %d" % fat)