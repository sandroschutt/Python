#-----VARIÁVEIS-----

lugaresOnibus = [
[0, 1, 0, 0],
[0, 0, 0, 1],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 0],
[0, 0, 1, 0],
[0, 0, 1, 0],
[0, 1, 0, 0],
[0, 1, 0, 0]]


#-----FUNÇÕES-----

def disponibilidadePoltronas(lugaresOnibus):
    contadorOcupados = 0
    contadorVazios = 0
    for i in range(0,10):
        for j in range(0,4):
            if lugaresOnibus[i][j] == 1:
                contadorOcupados += 1
            elif lugaresOnibus[i][j] == 0:
                contadorVazios += 1
    print("\nLugares ocupados: %d" % contadorOcupados,
        "\nLugares vazios: %d" % contadorVazios,
        "\nPorcentagem de ocupação: %.2f" % ((contadorOcupados / 40) * 100, "%"),
        "\n\nMAPA DAS POLTRONAS:\n")
    
    for i in lugaresOnibus:
        print(i)

def calculaArrecadacao(lugaresOnibus):
    contadorOcupados = 0
    for i in range(0,10):
        for j in range(0,4):
            if lugaresOnibus[i][j] == 1:
                contadorOcupados += 1
    print("\nLugares ocupados: %d" % contadorOcupados)
    janela = 0
    for i in range(0,10):
            if lugaresOnibus[i][0] == 1:
                janela += 1
            if lugaresOnibus[i][3] == 1:
                janela += 1

    arrecadacao = float(contadorOcupados * 50 - (janela * 50) + (janela * 55))
    print("\nArrecadação da viagem até agora: R$%.1f" % arrecadacao)

def verificaDisponibilidade (lugaresOnibus, selecionaLinha, selecionaColuna):
    if lugaresOnibus[selecionaLinha][selecionaColuna] == 1:
        print("\nPoltrona indisponível. Selecione outra poltrona.")
    else:
        print("\nParabéns, você acaba de reservar essa poltrona!")
        lugaresOnibus[selecionaLinha][selecionaColuna] = 1
        
        print("MAPA DAS POLTRONAS:\n\n")

        for i in lugaresOnibus:
            print(i)


#-----SAÍDA DE DADOS-----

x = 1
while x > 0:
    disponibilidadePoltronas(lugaresOnibus)

    selecionaLinha = int(input("\nEm qual linha deseja se sentar (0-9)? "))
    selecionaColuna = int(input("\nEm qual coluna deseja se sentar (0-3)? "))
    
    verificaDisponibilidade(lugaresOnibus, selecionaLinha, selecionaColuna)
    disponibilidadePoltronas(lugaresOnibus)
    calculaArrecadacao(lugaresOnibus)

    continuar = str(input("\nDeseja continuar (s/n): "))

    if continuar == "n":
        x = 0
