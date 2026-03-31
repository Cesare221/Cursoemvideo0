#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-=-=-=- Bem vindo ao analista de empréstimos -=-=-=-')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do salário do comprador? R$'))
anos = int(input('Em quantos anos deseja pagar?'))
prestaçao = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos, prestaçao))
if salario <= casa * 30 / 100:
    print('Seu impréstimo foi aprovado!')
else:
    print('Seu impréstimo foi negado!')
