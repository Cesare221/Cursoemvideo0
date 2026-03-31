#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Qual o valor do produto? R$ '))
d = v - (v * 5 / 100)
print('O produto de R${} com desconto fica R${:.2f}'.format(v, d))

