#faça um prog que leia o comp do cat oposto e do cat adj de um triangulo calcule e mostre a hipotenusa

from math import hypot

cat = float(input('Qual o comprimento do cateto oposto: '))
cat2 = float(input('Qual o comprimento do cateto adjacente: '))
print('o valor da hipotenusa é {}'.format(hypot(cat, cat2)))
