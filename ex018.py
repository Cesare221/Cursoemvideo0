#faça um prog que leia um angulo e mostre na tela valor do sen, coss e tang desse angulo

#f

#seno = sin(radians(10))
#cosseno = cos(radians(10))
#tanseno = tan(radians(10))
#print('a tangente do cateto e', tanseno)
#import math

# exemplo em graus
#angulo_graus = 45
#angulo_radianos = math.radians(angulo_graus)  # converte para radianos
#tangente = math.tan(angulo_radianos)
#print(f"A tangente de {angulo_graus}° é {tangente}")

from math import cos, sin, tan, radians
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O angulo de {} tem o cos de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O angulo de {} tem o tan de {:.2f}'.format(angulo, tan))
