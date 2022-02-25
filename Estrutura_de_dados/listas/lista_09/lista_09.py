#Gerar lista com 3 elementos; preencher lista; ordenar lista; exibir lista desordenada
#(índice, elemento); exibir lista ordenada (índice, elemento);

#-----VARIÁVEIS-----

palavras = [] * 3


#-----FUNÇÕES-----

def inserePalavra():
    for i in range(3):
        palavras.insert(i, str(input("Digite uma palavra: ")))
        
    print("\nExibe vetor desordenado\n")
    exibePalavra()
        
def ordenaListaPalavras():
    palavras.sort()
    for i in palavras:
        print(i)
        
    print("\nExibe vetor ordenado\n")
    exibePalavra()
    
def exibePalavra():
    for i in palavras:
        print("O valor no indice %i" % palavras.index(i), " é: %s" % i)
    print()
    

#-----SAÍDA DE DADOS-----

inserePalavra()
ordenaListaPalavras()
