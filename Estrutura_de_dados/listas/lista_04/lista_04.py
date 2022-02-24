#Criar função que gera vetor produto de dois vetores

vetorUm = [10, 20, 30, 40, 50]
vetorDois = [60, 70, 80, 90, 100]

def soma(vetorUm, vetorDois):
    vetorSoma = []
    for i in range(5):
        soma = vetorUm[i] + vetorDois[i]
        vetorSoma.append(soma)

    print('Vetor A: ', vetorUm,
        '\nVetor B: ', vetorDois,
        '\nVetor contendo a soma de Vetor A e Vetor B: ', vetorSoma)

soma(vetorUm, vetorDois)
