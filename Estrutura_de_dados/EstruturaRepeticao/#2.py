# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input('Nome de usuário: '))

gear = True
while gear == True:
    senha = str(input('Senha: '))
    if senha == nome:
        print('\nA senha não pode ser igual ao nome de usuário. Tente novamente.\n')
    else:
        print(f'\nUsuário: {nome}\nSenha: {senha}')
        gear = False