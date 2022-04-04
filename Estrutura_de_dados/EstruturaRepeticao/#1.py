# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

gear = True
while gear == True:
    num = int(input('Informe um número: '))
    if num >= 0 and num <= 10:
        print(f'O número informado foi: {num}')
        gear = False
    else:
        print('Número inválido. Tente novamente.\n')