# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = "SUBI NO ONIBUS"
fraseOriginal = frase #guarda a frase original

frase = list(frase) #transforma String frase em uma array sem espaços
fraseReversa = frase #prepara variável para reversão
fraseReversa.reverse() #reverte array sem alterar frase=[arr]

#transforma arrays em palavras sem espaços
frase = "".join(frase)
fraseReversa = "".join(fraseReversa)

#avalia se 'frase' é palíndroma
if frase == fraseReversa:
    print(f'A frase < {fraseOriginal} > é palíndroma')
else:
    print(f'A frase < {fraseOriginal} > não é palíndroma')