#5)programa que diga se o número informado é perfeito ou não.

numero = int(input(" informe um valor: "))
soma = 0
for i in range(1, numero):
    if(numero % i == 0):
        soma = soma + i
if (soma == numero):
    print(" %d é um número perfeito" %numero)
else:
    print(" %d não é um número perfeito" %numero)
