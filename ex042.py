print('ANALISADOR DE TRIÂNGULO')
print('=_'*15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo ', end='')
    if a == b == c:
       print('EQUILÁTERO!')
    elif a != b != c != a != c:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos NÃO podem formar um triângulo!')
    