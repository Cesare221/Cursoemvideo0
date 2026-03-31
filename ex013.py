#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual o valor do seu salário? R$ '))
a = s + (s * 15 / 100)
print('O seu salario de R$ {} com aumento fica R$ {:.2f}'.format(s, a))

