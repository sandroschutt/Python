#18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

volumeArquivo = float(input('Informe o tamanho do arquivo a ser baixado(MB): '))
velocidadeLink = float(input('Informe a velocidade da banda(Mbps): '))

volumeMb = volumeArquivo * 8
print(f'Tempo estimado para conclusão do download: {(volumeMb / velocidadeLink) / 60: .2f}min')