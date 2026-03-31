#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
#a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura

print('A largura da sua parede é: {} x {} e a área é: {}m²'.format(largura, altura, area))
print('Você precisará de {}L de tinta para pintar essa parede'.format(area / 2))
