# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

paisA = int(80000)
paisB = int(200000)

contador = 0

gear = True
while gear == True:
    paisA += paisA * .03
    paisB += paisB * .015
    contador += 1
    if paisA > paisB:
        print(f'Tempo estimado para população de País A superar a de País B: {contador} anos.\nPopulação de País A no referido ano: {paisA: .0f}\nPopulação de País B no referido ano: {paisB: .0f}')
        gear = False