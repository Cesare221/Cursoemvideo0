# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
print('=_'*15)
print('ANALISADOR DE TRIANGULO')
print('=_'*15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar triangulo')
else:
    print('Os segmentos NAO podem formar triangulo')
