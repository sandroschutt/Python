# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def inverteNumero(nx):
    nx.reverse()
    separator = "".join(nx)
    print(f'Nº invertido: {separator}')

n = str('127')
nx = list(n)
inverteNumero(nx)