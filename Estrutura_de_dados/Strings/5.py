# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = "FULANO"
nome = list(nome)

for i in range(len(nome)):
    print("".join(nome))
    nome.pop()