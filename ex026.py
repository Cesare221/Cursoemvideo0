#Faça um programa que leia uma frase e mostre:
#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
