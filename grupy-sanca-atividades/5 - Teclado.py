print()

#1
nome = input('Digite seu nome: ')
print('Olá {nome}'.format(nome = nome))
nome1 = input('Digite outro nome: ')
print('{nome} roubou pão na cassa do {nome1}!'.format(nome = nome, nome1 = nome1))
print('{nome1} ficou triste e com fome, porque o bandeijão estava fehado!'.format(nome1 = nome1))
print('------------------------------------------------------------------------------------------------')

#2 

frase = input('Digite uma frase: ')
print('A frase alcontrario é assim: ')
print(frase[::-1])
print('------------------------------------------------------------------------------------------------')
