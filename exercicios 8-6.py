print()

#1

frase = 'Python é muito legal.'
palavra1 = frase[0:6]
palavra2 = frase[7:8]
palavra3 = frase[9:14]
palavra4 = frase[15:20]
print(frase)
print(palavra1)
print(palavra2)
print(palavra3)
print(palavra4)
print('------------------------------------------------------------------------------------------------')

#2

print('O tamanho de "{a}" é {b}'.format(a = frase,b = len(frase)) )
print('O tamanho de "{a}" é {b}'.format(a = palavra1,b = len(palavra1)) )
print('O tamanho de "{a}" é {b}'.format(a = palavra2,b = len(palavra2)) )
print('O tamanho de "{a}" é {b}'.format(a = palavra3,b = len(palavra3)) )
print('O tamanho de "{a}" é {b}'.format(a = palavra4,b = len(palavra4)) )
print('------------------------------------------------------------------------------------------------')

#3

palavra1,palavra2,palavra3,palavra4 = str.split(frase)
print(frase)
print(palavra1)
print(palavra2)
print(palavra3)
print(palavra4)
print('------------------------------------------------------------------------------------------------')

#4

print(palavra1[::-1])
print('------------------------------------------------------------------------------------------------')
    