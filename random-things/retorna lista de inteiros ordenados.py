def ordenar_inteiros_numa_lista(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    lista.sort()
    return lista

print(ordenar_inteiros_numa_lista([5,4,3,2,1]))

'''
    UMA FORMA MAIS EFICIENTE DE ORDENAR AS LISTAS DE NUMEROS DOS EXERCICIOS 16.8 É UTILIZAR ESSA FUNÇÃO
'''
