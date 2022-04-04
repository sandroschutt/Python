#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Entre com um número inteiro: "))
for valor in range(2,num):
    if num % valor == 0 or num == 1:
        print(num,"não é primo")
        break
    else:
        print(num,"é primo")