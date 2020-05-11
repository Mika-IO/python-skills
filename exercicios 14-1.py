print()

#1

print()
for i in range (1,11):
    print(13,'X',i,'=',13*i)
print('------------------------------------------------------------------------------------------------')

#2

print()
while True:
    try:
        lista_numeros = input('Digite cinco numeros separados ')  
        lista_numeros = lista_numeros.split()
        if len(lista_numeros) == 5:
            break
        else:
            print('Tem que ser 5 numeros.')
    except:
        print('Algo de errado')
for i in range(len(lista_numeros)):
    lista_numeros[i] = int(lista_numeros[i])
lista_numeros.sort()
print('O menor número é: ',lista_numeros[0])
print('------------------------------------------------------------------------------------------------')


#3

print()
while True:
    try:
        lista_numeros = input('Digite cinco numeros separados ')
        lista_numeros = lista_numeros.split()
        if len(lista_numeros) == 5:
            break
        else:
            print('Tem que ser 5 numeros.')
    except:
        print('Algo deu errado... Talvez você não tenha digitado números..')
for i in range(len(lista_numeros)):
    lista_numeros[i] = int(lista_numeros[i])
lista2 = lista_numeros.sort()
if lista_numeros == lista2: 
    print(True)
else:
    print(False)
print('------------------------------------------------------------------------------------------------')

#4

print()
a=500
for i in range(491):
    print(a)
    a = a - 1
print('------------------------------------------------------------------------------------------------')

#5

print()
while True:
    try:
        lista_numeros = input('Digite 10 numeros separados ')
        lista_numeros = lista_numeros.split()
        for i in range(len(lista_numeros)):
            lista_numeros[i] = int(lista_numeros[i])
        if len(lista_numeros) == 10:
            break
        else:
            print('Tem que ser 10 numeros.')
    except:
        print('Algo deu errado... Talvez você não tenha digitado números..')
contador = 0
for i in range(len(lista_numeros)):
    if lista_numeros[i] > 10 and lista_numeros[i] < 50:
        contador = contador + 1
print('Foram digitados {contador} numeros entre 10 e 50'.format(contador=contador))
print('------------------------------------------------------------------------------------------------')

#6

print()
idade_homens = 0
idade_mulheres = 0
homens = 0
mulheres = 0
for i in range(11): 
    print('Pessoa',i)
    print('Digite M para homens e F para mulheres')
    while True:  
        sexo = input('Sexo: ')
        sexo = sexo.upper()
        while True:
            try:
                idade = int(input('Idade: '))
                break
            except:
                print('A idade é um número animal')
        
        if sexo == 'M':
            homens = homens + 1
            idade_homens = idade_homens + idade
            break
        elif sexo == 'F':
            mulheres = mulheres + 1
            idade_mulheres = idade_mulheres + idade
            break
        else:
            print('Digite algo válido')
print('Idade média das mulheres: ',idade_mulheres/mulheres)
print('Idade média dos homens: ',idade_homens/homens)
print('Idade média do grupo: ',(idade_homens+idade_mulheres)/(homens+mulheres))
print('------------------------------------------------------------------------------------------------')

#7

print()
soma = 0
for i in range(0,101):
    soma = soma + i
print('A soma de todos os numeros de 0 a 100 é ',soma)
print('------------------------------------------------------------------------------------------------')

