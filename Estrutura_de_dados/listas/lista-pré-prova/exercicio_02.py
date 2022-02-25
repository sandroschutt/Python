def CriaQuadro():
    dimensao = int(input("Informe a dimensão do quadro (x * y): "))
    dimensao *= dimensao
    foto = int(input("Informe o tamanho da foto (x * y): "))
    foto *= foto
    quantidadeFotos = int(input("informe a quantidade de fotos\na serem colocados no quadro: "))
    foto *= quantidadeFotos
    print("\nAs fotos irão ocupar um total de %d blocos no quadro." % foto,
        "\nDimensão do quadro: %d" % dimensao,
        "\nTamanho de cada foto: %d" % (foto / quantidadeFotos),
        "\nQuantidade de fotos: %d" % quantidadeFotos) 

CriaQuadro()
