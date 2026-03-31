#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero que eu adivinharei se ele é par ou ímpar: '))
if num % 2 == 0:
    print('Seu numero {} par'.format(num))
else:
    print('Seu numero {} impar'.format(num))
print('-=-' * 10)
print('FIM')
print('-=-' * 10)
7