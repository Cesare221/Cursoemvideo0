#Crie um programa que leia o nome de uma pessoa e mostre:
# nome com todas as letras maiusculas
#o nome com todas minusculas
#quantas letras ao todo sem espaço
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Minúsculo: ', nome.lower())
print('Maiúsculo: ', nome.upper())
print('Qtde de letras: ', len(nome) - nome.count(' '))
print('Letras do primeiro nome: ', nome.find(' '))