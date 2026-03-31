"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
atual = date.today().year

ano = int(input('Informe o ano de nascimento: '))
sexo = input('Informe o sexo [M/F]: ').strip().upper()
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,atual))
if sexo == 'M':
 if idade == 18:
    print('Você tem que se alistar!')
 elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos para o alistamento.'.format(saldo))
    a = atual + saldo
    print('Seu alistamento será em {}.'.format(a))
 elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    a = atual - saldo
    print('Seu alistamento foi em {}.'.format(a))
elif sexo == 'F':
    print('O alistamento não é obrigatório para mulheres.')
