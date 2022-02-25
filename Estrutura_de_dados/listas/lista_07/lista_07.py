#Fatoração com função de loop e função recursiva

numero = 5
contador = 5

def funcaoLoop(numero, contador):
    while contador > 1:
        contador = contador - 1
        fatorial = numero * contador
        print("5! | ", numero, " * ", contador, " = ", fatorial)
        numero = fatorial

def funcaoRecursiva(numero, contador):
    if contador > 1:
        contador = contador - 1
        fatorial = numero * contador
        print("5! | ", numero, " * ", contador, " = ", fatorial)
        numero = fatorial
        funcaoRecursiva(numero, contador)

print("Função com loop:")
funcaoLoop(numero,contador)
print("\nFunção recursiva:")
funcaoRecursiva(numero,contador)
