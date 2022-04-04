# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

numero = str(input('Nº: '))
numero = list(numero)

while (len(numero)) != 9:
    if (len(numero)) < 9:
        numero.append('3')
    if (len(numero)) > 9:
        numero.pop()

numeroFormatado = "".join(numero)

print(f'Nº celular: +55 (55) {numeroFormatado}')