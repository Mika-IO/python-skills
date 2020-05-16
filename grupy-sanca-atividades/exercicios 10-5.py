print()

#1
print()
lista = ['Leticia','Rodrigo','Jheny']
print('------------------------------------------------------------------------------------------------')

#2

print()
frutas = ['Banana','Morango','Maça']
docinhos = ['Bolo','Brigadeiro','Balas']
ingreJeijoada = ['Feijão','Carne de porco','Sal','Alho']
listona = [frutas,docinhos,ingreJeijoada]
print(listona[1][1])    
docinhos.insert(1,'Brigadeiro')
print(listona)
listona.append('bebidas')
print(listona)
print('------------------------------------------------------------------------------------------------')

#3

print()
i = 0
for i in range(len(listona)):
    del listona[0]
print(listona)
print('------------------------------------------------------------------------------------------------')

#4

print()
lista_compras = ['Bebidas','Arroz','Feijão','Produtos de limpeza','Sorvetes']
print(lista_compras)
del lista_compras[-1]
del lista_compras[-1]
print(lista_compras)
print('------------------------------------------------------------------------------------------------')

#5

print()
lista_numeros = [4,5,3,7,8,3,2,1,4,6,4,2,5,7,9,77,8,9,22,33,35,4,345]
print('Lista de numeros desordenados:  ',lista_numeros)
lista_numeros.sort()
print('Lista de numeros ordenados:     ', lista_numeros)
def inverter(lista):
    for i in range(0,len(lista)):
        lista.insert(i,lista[-1])
        del lista[-1]
    return lista
lista_numeros = inverter(lista_numeros)
print('Lista invertida:                ',lista_numeros)
print('------------------------------------------------------------------------------------------------')

