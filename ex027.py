#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer! {}'.format(nome[0]))
print('Sobrenome: {}'.format(nome[len(nome)-1]))
