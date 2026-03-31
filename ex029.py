#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km = float(input('Qual a velocidade do carro? '))
if km > 80:
    print('Você está acima da velocidade permitida e foi multado.')
    print('Terá que pagar uma multa de R$ {:.2f}'.format((km - 80) * 7))
else:
    print('Esta dentro dos limites da via, siga com segurança.')
