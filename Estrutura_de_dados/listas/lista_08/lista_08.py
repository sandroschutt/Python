#ANALISA E CIFRA PALAVRA INFORMADA

#-----FUNÇÕES-----
def analisaPalavra():
     vogais = [[0],[0],[0],[0],[0]] #índice [0] = A, índice [1] = E...
     print("A frase informada foi:", palavraInformada)
     qtdchar = len(palavraInformada)

     palavra = list(palavraInformada.upper())

     qtdVogais = 0
     qtdConsoantes = 0

     for i in range(len(palavra)):
        if palavra[i] == 'A':
            qtdVogais += 1
            vogais[0][0] += 1
        elif palavra[i] == 'E':
            qtdVogais += 1
            vogais[1][0] += 1
        elif palavra[i] == 'I':
            qtdVogais += 1
            vogais[2][0] += 1
        elif palavra[i] == 'O':
            qtdVogais += 1
            vogais[3][0] += 1
        elif palavra[i] == 'U':
            qtdVogais += 1
            vogais[0][0] += 1
        elif palavra[i] == " ":
            qtdchar -= 1
        else:
            qtdConsoantes += 1

     print("A quantidade de letras é %i" % qtdchar,
        "\nNº vogais: ", qtdVogais,
        "\nNº consoantes: ", qtdConsoantes,
         "\n\nOcorrência de vogais:", "\nA = ",vogais[0],
         "\nE = ", vogais[1],
         "\nI = ", vogais[2],
         "\nO = ", vogais[3],
         "\nU = ", vogais[4])
         
     cifraPalavra(palavra)

def cifraPalavra(palavra):
    vogais = "A E I O U"
    listaVogais = vogais.upper().split()
    consoantes = "B C D F G H J K L M N O P Q R S T V W X Y Z"
    listaConsoantes = consoantes.upper().split()
    variavelCifrada = ""

    for i in palavra:
        if i in listaVogais:
            cifraVogal = ord(i) + 3
            variavelCifrada += chr(cifraVogal)
        elif i in listaConsoantes:
            cifraConsoantes = ord(i) + 6
            variavelCifrada += chr(cifraConsoantes)

    print("\nFrase normal: %s" % palavraInformada,
        "\nFrase cifrada: %s" % variavelCifrada)


#-----ENTRADA DE DADOS-----
print("Informe uma frase qualquer: ")
palavraInformada = str(input())


#-----SAÍDA DE DADOS-----
analisaPalavra()
