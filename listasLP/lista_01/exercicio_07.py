idades = []
x = 1
while x:
    idade = int(input('Digite uma idade ou 0 para mostrar a média de idades: '))
    if idade > 0:
        idades.append(idade)
    else:
        x = 0

print('A média de idade é: ', sum(idades) / len(idades))
