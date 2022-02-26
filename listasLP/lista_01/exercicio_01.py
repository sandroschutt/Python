#Escreva um programa que leia um conjunto de 10 números inteiros. Calcule e mostre:
#a)o menor número
#b)a soma dos números pares e maiores que 10
#c)a quantidade de números ímpares
#d)a média dos números maiores que 20

soma = 0
media = 0
contador = 0
impares = 0
lista = []

for i in range(10):
    numero = int(input("Digite um número: "))

    lista.append(numero)

    if numero > 10 and numero % 2 == 0:
        soma = soma + numero
    if numero % 2 != 0:
        impares = impares+1
    if numero > 20:
        contador = contador+1

    media = media + numero

print(lista)
print("O menor número da sua lista: ", min(lista))
print("A soma dos números pares e maiores que 10: ", soma)
print("A quantidade de números ímpares: ", impar)
print("A media dos números maiores que 20 eh: ", media/contador)
