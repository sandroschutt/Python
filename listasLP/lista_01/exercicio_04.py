#4)Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme (3-ótimo;2-bom;1-regular)
#Faça  um  programa  que  receba  a  idade  e  a  opinião  de  um  número  indeterminado  de
#pessoas. Para finalizar a entrada deve ser digitado uma idade negativa ou zero. Calcule e mostre:
#A média das idades das pessoas que responderam ótimo;
#A quantidade de pessoas que responderam regular;
#A quantidade de pessoas que responderam bom.

otimo = 0
bom = 0
regular = 0
mediaOtimo = 0

idade = int(input("Olá, qual é a sua idade? ")
while idade > 0:
    opiniao = str(input("Na sua opinião, o filme foi:: ótimo(3), bom(2) ou regular(1)?: "))
    if opiniao == '1':
        otimo = otimo + 1
        mediaOtimo += idade
    elif opinião == '2':
        bom += 1
    elif opinião == '3':
        regular += 1
    else:
        print("Opinião inválida. Você deve digitar/escrever somente entre as seguintes opções: Ótimo, bom ou regular. Tente de novo!")

    idade = int(input("Qual é a sua idade?"))

print("A média das pessoas que responderam 'ótimo' é: ", mediaOtimo/otimo)
print("A quantidade de pessoas que responderam 'regular' é: ", bom)
print("A quantidade de pessoas que responderam 'bom' é: ", regular)
