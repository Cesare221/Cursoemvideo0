"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM                     – Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR                   – Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if nasc <= 9:
    print('O atleta de {} anos, está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta de {} anos, está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta de {} anos, está na categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta de {} anos, está na categoria SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta de {} anos, está na categoria MASTER'.format(idade))
