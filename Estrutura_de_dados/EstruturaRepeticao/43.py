#O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100 1,20
# Bauru Simples 101 1,30
# Bauru com ovo 102 1,50
# Hambúrguer 103 1,20
# Cheeseburguer 104 1,30
# Refrigerante 105 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio =[['Cachorro Quente', '100', 1.20],['Bauru Simples', '101', 1.30], ['Bauru com ovo', '102', 1.50],['Hambúrguer', '103', 1.20],['Cheeseburguer', '104', 1.30],['Refrigerante', '105', 1.00]]

totalPagar = []
for i in cardapio:
    print(f'Especificação: {i[0]}  Cod: {i[1]}  Preço: R${i[2]: .2f}')

gear = True
while gear == True:
    lanche = str(input('\nEscolha um lanche (cod): '))
    qtdLanches = int(input('Quantos lanches deseja comprar? '))
    for i in cardapio:
        if lanche == i[1]:
            lancheSelecionado = i[0]
            preco = qtdLanches * i[2]
            totalPagar.append(preco)

            continuar = str(input('Deseja comprar mais algum lache (s/n)? '))
            
            saidaDados = print(f'Pedido: {qtdLanches}x  {lancheSelecionado}  Cod: {lanche}  Preço: R${preco: .2f}')

            gear = True if continuar == 's' else False

print(f'\nTOTAL A PAGAR: R${sum(totalPagar): .2f}')