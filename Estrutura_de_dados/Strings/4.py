# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = "FULANO"
nome = list(nome)
pilha = []

for i in nome:
    pilha.append(i)
    escada = "".join(pilha)
    print(escada)