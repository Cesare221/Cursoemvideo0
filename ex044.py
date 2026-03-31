"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:  – à vista dinheiro/cheque: 10% de desconto
 – à vista no cartão: 5% de desconto  – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros"""
print('{:=^40}'.format(' Cesare store '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/pix
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual das opções acima: '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção== 4:
    total = preco + (preco * 20 / 100)
    toralparc = int(input('Quantas parcelas serão? '))
    parcela = total / toralparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(toralparc, parcela))
else:
    total = 0
    print('Opção errada! Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, total))
