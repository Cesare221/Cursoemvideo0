#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de km percorrido: '))
dia = float(input('Qual a quantidade de dias percorrido: '))
a = (dia * 60) + (km * 0.15)
print('Com os {}km e os {} dias o valor do aluguel do veículo ficou em R$ {:.2f}'.format(km, dia, a))

