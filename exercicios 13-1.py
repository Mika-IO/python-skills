print()

#1

print()
while True:
    try:
        n1=int(input('Digite o primeiro numero: '))
        n2=int(input('Digite o segundo numero: '))
        break
    except:
        print('Tem que digitar um numero')
        print()
if n1 > n2:
    print('O primeiro é o maior')
if n2 > n1:
    print('O segundo é o maior')
else:
    print('OS dois são iguais')
print('------------------------------------------------------------------------------------------------')

#2

print()
while True:
    try:
        idade=int(input('Quantos anos você tem? '))
        peso=int(input('Quanto você pesa em kilogramas? '))
        hrsdurmidas=int(input('Quanto você durmiu nas ultimas 24 horas? '))
        break
    except:
        print('Todas as respostas devem ser numeros')
        print()
if idade > 16 and idade < 69 and peso > 50 and hrsdurmidas > 6:
    print('Você pode doar sangue')
else:
    print('Você não pode doar sangue')
print('------------------------------------------------------------------------------------------------')

#3

print()
a = int(input('Digite o coeficiente a: '))
b = int(input('Digite o coeficiente b: '))
c = int(input('Digite o coeficiente c: '))        # EU NÃO TENHO CERTEZA  
delta = (b**2) - 4 * a * c                        # QUE ESTEJA CORRETO
if delta > 0:
    print('Possui duas raizes')
elif delta < 0:
    print('Não possui raiz real')
else:
    print('Possui uma raiz')
print('------------------------------------------------------------------------------------------------')

#4

print()
a = int(input('Digite o numero a: '))
b = int(input('Digite o numero b: '))
soma = a + b
if soma > 20:
    print('Resultado da soma mais 8 é ',soma+8)
elif soma <= 20:
    print('Resultado soma menos 5 é ',soma-5)

print('------------------------------------------------------------------------------------------------')

#5

print()
a = int(input('Digite o numero a: '))
if a >= 0:
    from math import sqrt
    print('A raiz quadrada de {a}'.format(a=sqrt(a)))
else:
    print('O quadrado de {a}'.format(a=a**2))
print('------------------------------------------------------------------------------------------------')

#6

print()
while True:
    a = int(input('Escolha um mês por um numero: '))   
    if a>0 and a<13:
        break
    else:
        print('O numero tem que ser de 1 a 12...')
if a==1:
    print('JANEIRO')
elif a==2:
    print('FEVEREIRO')
elif a==3:
    print('MARÇO')
elif a==4:
    print('ABRIL')
elif a==5:
    print('MAIO')
elif a==6:
    print('FEVEREIRO')
elif a==7:
    print('JUNHO')
elif a==8:
    print('JULHO')
elif a==9:
    print('AGOSTO')
elif a==10:
    print('SETEMBRO')
elif a==11:
    print('OUTUBRO')
elif a==12:
    print('NOVEMBRO')
print('------------------------------------------------------------------------------------------------')