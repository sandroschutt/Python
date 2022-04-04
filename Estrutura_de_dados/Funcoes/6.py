# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

hora = int(input('Hora (00~24h): '))
minuto = int(input('Minutos (00~60): '))

def converteHorario(hora, minuto):
    aMpM = 'AM' if hora < 12 or hora == 24 else 'PM'

    horas12 = []
    for i in range(13):
        horas12.append(i)

    horas24 = []
    for i in range(12,25):
        horas24.append(i)

    for i in range(13):
        if hora == horas24[i]:
            hora = horas12[i] if hora != 24 else 0

    saidaDados(hora, minuto, aMpM)

def saidaDados(hora12, minuto, aMpM):
    print(f'Hora convertida(12h): {hora12: .0f}:{minuto} {aMpM}')

converteHorario(hora, minuto)