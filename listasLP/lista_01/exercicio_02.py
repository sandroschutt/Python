#Faça um programa que receba dez números inteiros. Calcule e mostre:
#A soma dos números primos
#A média dos números múltiplos de 3 que são maiores que 10

qtdNumerosPrimos = 0
qtdNumerosMultiplosTres = 0
somaNumerosPrimos = 0
somaNumerosMultiplosTres = 0

for i in range(10):
    numero = int(input("Escreva um número: "))
    for i in range (1, numero + 1):
        if numero % i == 0:
            qtdNumerosPrimos = qtdNumerosPrimos + 1
    if qtdNumerosPrimos == 2:
        somaNumerosPrimos = somaNumerosPrimos + numero
    if numero % 3 == 0 and numero >10:
        qtdNumerosMultiplosTres = qtdNumerosMultiplosTres + 1
        somaNumerosMultiplosTres = somaNumerosMultiplosTres + numero

print("Soma dos numeros primos: ", qtdNumerosPrimos)
print("A media dos numeros multiplos de 3 que são maiores que 10:", somaNumerosMultiplosTres/qtdNumerosMultiplosTres)
