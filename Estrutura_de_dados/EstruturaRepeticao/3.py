# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

gearNome = True
while gearNome == True:
    nome = str(input('Nome: '))
    if len(nome) > 3:
        gearNome = False

gearIdade = True
while gearIdade == True:
    idade = int(input('Idade: '))
    if idade > 0  and idade <= 150:
        idade = idade
        gearIdade = False

gearSalario = True
while gearSalario == True:
    salario = int(input('Salário: '))
    if salario > 0:
        salario = salario
        gearSalario = False

gearSexo = True
while gearSexo == True:
    sexo = str(input('Sexo (m/f): '))
    if sexo == 'm':
        sexo = 'Masculino'
        gearSexo = False
    if sexo == 'f':
        sexo = 'Feminino'
        gearSexo = False

gearES = True
while gearES == True:
    estadoCivil = str(input('Estado Civil ([s]solteiro; [c]casado; [v]viúvo; [d]divorciado): '))
    if estadoCivil == 's':
        estadoCivil = 'Solteiro(a)'
        gearES = False
    elif estadoCivil == 'c':
        estadoCivil = 'Casado(a)'
        gearES = False
    elif estadoCivil == 'v':
        estadoCivil = 'Viúvo(a)'
        gearES = False
    elif estadoCivil == 'c':
        estadoCivil = 'Divorciado(a)'
        gearES = False

print(f'\nNome: {nome}\nIdade: {idade}\nSexo: {sexo}\nSalário: {salario}\nEstado Civil: {estadoCivil}')