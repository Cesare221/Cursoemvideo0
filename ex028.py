#Escreva um programa que faça o computador “pensar” em um
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#num = (float(input('Digite um numero de 0 a 5 e veja se adivinhou: ')))
#n = num.randint(1, 10)
#print('PROCESSANDO...')
#print('O numero escolhido foi {}'.format(n))

from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(5)
if jogador == comp:
    print('PARABÉNS!! Voce conseguiu me vencer!')
else:
    print('Voce perdeu! Eu pendei no número {} e nao no {}'.format(comp, jogador))
    print('-=-' * 20)