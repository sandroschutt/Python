#Usar funções void para aplicar calculos específicos em cima de valores informados pelo usuário

def fsoma():
    numero = int(input("Informe um número qualquer: "))
    resultado = numero + 30
    print('%.2d + 30 = ' % numero, resultado)

def fsub():
    numero = int(input("Informe um número qualquer: "))
    resultado = numero - 10
    print('%.2d - 10 = ' % numero, resultado)

def fdiv():
    numero = int(input("Informe um número qualquer: "))
    resultado = numero / 2
    print('%.2d / 2 = ' % numero, resultado)

def fmult():
    numero = int(input("Informe um número qualquer: "))
    resultado = numero * 5
    print('%.2d * 5 = ' % numero, resultado)

def fcub():
    numero = int(input("Informe um número qualquer: "))
    resultado = numero * numero * numero
    print('%.2d ^ 3 = ' % numero, resultado)

fsoma()
fsub()
fdiv()
fmult()
fcub()

print("Programa encerrado.")
