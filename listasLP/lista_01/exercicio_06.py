numero = int(input('Informe um número para o fatorial: '))
x = numero
fatorial = 1
while x > 0:
    print('{}' .format(x))
    fatorial *= x
    x -= 1
    
print('O resultado do fatorial é {}' .format(fatorial))
