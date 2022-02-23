#6)Faça um programa que percorra duas listas e gere uma terceira lista sem os elementos
#repetidos. Mostra na tela as 3 listas.

listaUm = []
listaDois = []
listaFinal = []

print('*DIGITE 0 PARA ENCERRAR O PROGRAMA*')

encerraPrograma = 1
while encerraPrograma > 0:
    numeroA = int(input('Insira um número na lista A: '))
    if numeroA > 0:
        listaUm.append(numeroA)
        listaFinal.append(numeroA)
    else:
        encerraPrograma = 0

encerraPrograma = 1
while encerraPrograma > 0:
    numeroB = int(input('Insira um número na lista B: '))
    if numeroB > 0:
        listaDois.append(numeroB)
        listaFinal.append(numeroB)
    else:
        encerraPrograma = 0

def removeRepetidos(listaFinal):
    listaSemRepeticao = []
    for i in listaFinal:
        if i not in listaSemRepeticao:
            listaSemRepeticao.append(i)
    listaSemRepeticao.sort()
    return listaSemRepeticao

print('Lista 01: ', listaUm, '\nLista 02: ', listaDois, '\nLista sem elementos repetidos: ', removeRepetidos(listaFinal))
