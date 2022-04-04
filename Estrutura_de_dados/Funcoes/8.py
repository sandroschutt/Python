# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def qtdDigitos(numero):
    numero = str(numero)
    nDigitos = len(numero)
    print(f'Nº: {numero}  Qtd digitos: {nDigitos}')

numero = int(input('Nº: '))

qtdDigitos(numero)