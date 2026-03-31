#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
T = float(input('Qual a temperatura em °C: '))
F = ((9 * T) / 5) + 32
print('A temperatura de {}°C em fahrenheit é de {}°F'.format(T, F))

