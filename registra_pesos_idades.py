#Faça um programa que receba a idade e os
#respectivos pesos de um número indeterminado
#de pessoas. Para finalizar a entrada deve ser
#digitado idade zero ou negativa.
#Calcule e mostre na tela:
#A maior idade
#A quantidade de pessoas que pesam mais que
#90 quilos.
#A média de idade das pessoas que pesam
#menos que 50 quilos.

listaIdade = []
ListaPesosPesados = []
idadePessoasLeves = []
idade = int(input("Informe a idade: "))
peso = int(input('Informe o peso: '))
while idade > 0:
    listaIdade.append(idade)
    if peso > 90:
        ListaPesosPesados.append(peso)
    elif peso < 50:
        idadePessoasLeves.append(idade)
    idade = int(input("Informe a idade: "))
    peso = int(input('Informe o peso: '))

print('Maior idade: ', max(ListaIdade))
print('Qtd de pessoas que pesam mais de 90kg: ', len(ListaPesosPesados))
print('Média de idade das pessoas com menos de 50kg: ', (sum(idadePessoasLeves)/len(idadePessoasLeves)))
