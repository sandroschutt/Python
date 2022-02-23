#soma = 0
totalPrimos = 0
somaImpar = 0
somaPar = 0 
contadorPares = 0

for c in range(0,10):
    numero = int(input("Digite um número: "))

    if numero % 2 != 0:
        somaImpar += numero

    if numero % 2 == 0:
        contadorPares += 1
        somaPar += numero

    #for d in range(1, numero + 1):
    #    if numero % d == 0:
    #        soma += 1

    if soma == 2 or numero == 1:
        totalPrimos += 1
    #soma = 0

mediaPares = somaPar / contadorPares
print(f'A quantidade de números primos é {totalPrimos}')
print(f'A soma dos números impares é: {somaImpar}')
print(f'A média dos números pares é {mediaPares}')
