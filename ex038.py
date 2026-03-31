#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
print('\033[0;36;40m^\033[m'*21)
print('\033[7;40mComparador de números\033[m')
print('\033[0;36;40m^\033[m'*21)
n1 = int(input('\033[7;40mDigite o primeiro número: \033[m'))
n2 = int(input('\033[7;40mDigite o segundo número: \033[m'))
if n1 > n2:
    print('\033[7;40mO primeiro valor é maior!\033[m')
elif n2 > n1:
    print('\033[7;40mO segundo valor é maior\033[m')
else:
    n1 = n2
    print('\033[7;40mOs números são iguais!\033[m')
    
