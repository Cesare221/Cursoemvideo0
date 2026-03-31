#Crie um prog que leia o nome de uma cidade e diga se ela começa ou nao com nome "SANTO"
cid = str(input('Em que cidade vc nasceu: ')).strip()
print(cid[0:5].upper() == 'SANTO')

