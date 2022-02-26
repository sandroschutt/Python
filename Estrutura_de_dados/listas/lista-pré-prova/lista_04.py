def CifraSenha (frase, alfabeto):
    senhaCifrada = []
    frase = list(frase)
    for i in range(len(frase)):
        if frase[i] in alfabeto:
            cifra = ord(frase[i]) + 3
            variavelCifrada = chr(cifra)
            senhaCifrada.append(variavelCifrada)
        else:
            cifra = ord(frase[i]) + 2
            variavelCifrada = chr(cifra)
            senhaCifrada.append(variavelCifrada)
    print(senhaCifrada)

alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
frase = str(input("Informe a senha a ser cifrada: ").upper())
CifraSenha(frase, alfabeto)
