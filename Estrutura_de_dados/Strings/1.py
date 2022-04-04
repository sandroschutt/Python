# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

fraseA = "Brasil Hexa 2006"
fraseB = "Brasil! Hexa 2006"

def tamanhoString(fraseA, fraseB):
    stringA = int(len(fraseA))
    stringB = int(len(fraseB))
    if stringA == stringB:
        saida = "As duas strings possuem o mesmo tamanho."
    else:
        saida = "As duas strings são de tamanhos diferentes"
    return saida

def conteudoString(fraseA,fraseB):
    saida = "As duas strings possuem conteúdo diferente" if fraseA != fraseB else "As duas strings possuem o mesmo conteúdo"
    return saida

print(f'String 1: {fraseA}\nString 2: {fraseB}\nTamanho de <{fraseA}>: {len(fraseA)} caracteres\nTamanho de <{fraseB}>: {len(fraseB)} caracteres\n{tamanhoString(fraseA,fraseB)}\n{conteudoString(fraseA,fraseB)}')