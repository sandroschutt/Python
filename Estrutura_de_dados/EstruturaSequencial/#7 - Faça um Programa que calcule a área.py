#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# area = altura * largura

dimensao = int(input('Informe a altura do quadrado: '))

area = dimensao * dimensao

print(f'O quadrado informado é de ordem {dimensao}x{dimensao}\nSua área é de {area}\nO dobro de sua área é {area * 2}')