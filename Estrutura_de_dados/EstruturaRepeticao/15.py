#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

fibonacci = [1]

n = int(input('Informe um parâmetro para a sequência de Fibonacci: '))

for i in range(1, n):
    if i == 1:
        fibonacci.append(i)
        fibonacci.append(fibonacci[0] + fibonacci[i])
        i = 3
    else:
        resultante = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(resultante)

print(f'Sequência de Fibonacci: {fibonacci}')