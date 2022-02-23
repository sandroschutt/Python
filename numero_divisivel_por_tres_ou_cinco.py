#Faça um algoritmo que receba um número e
#verifique se esse número é divisível por 3 e 5.
#Exibindo a mensagem na tela se o número é
#ou não divisível por 3 e 5.

numero = int(input('Insira um número: '))
if numero % 2 == 0:
    print('O número %d é divisível por 3 ou 5.' % numero)
else:
    print('O número %d não é divisível por 3 ou 5.'% numero)
