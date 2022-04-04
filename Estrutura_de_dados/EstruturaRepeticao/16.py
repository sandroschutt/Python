#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

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
        if resultante > 500:
            break

print(f'Sequência de Fibonacci: {fibonacci}')