def calculaColisao(cenario):
    colide = []
    for i in range(4):
        if cenario[1][i] - cenario[0][i] >= 2:
            saida = 0
            colide.append(saida)
        else:
            saida = 1
            colide.append(saida)
    colisao = sum(colide)
    if colisao == 3 or colisao == 4:
        print(1)
    else:
        print(0)

cenario1 = [[0, 0, 1, 1],[0, 0, 1, 1]]
cenario2 = [[0, 0, 2, 2],[1, 1, 3, 3]]
cenario3 = [[0, 0, 1, 1],[2, 2, 3, 3]]

calculaColisao(cenario1)
calculaColisao(cenario2)
calculaColisao(cenario3)
