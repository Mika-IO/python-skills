from math import pi
from sys import exit

def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao_real(a,b):
    return a/b
def divisao_inteira(a,b):
    return a//b
def resto_divisao(a,b):
    return a%b
def potencia(a,b):
    return a**b
def fatorial(n): 
    x = 0
    n+=1
    for i in range(n):
        x+=i
    return x

def menor_da_lista(n): 
    x=n[0] 
    for i in range(len(n)):
        if n[i] < x:
            x=n[i]
def area(r):
    a = pi * r**2
    return a
def valor_absoluto(x):
    if x < 0:
        return -x
    else:
        return x

while True:
        print('--------------------------')
        print('CALCULADORA')
        print('1 - SOMA')
        print('2 - SUBTRAÇÃO')
        print('3 - MULTIPLICAÇÃO')
        print('4 - DIVISÃO REAL')
        print('5 - DIVISÃO INTEIRA')
        print('6 - RESTO DA DIVISÃO')
        print('7 - POTÊNCIA')
        print('8 - FATORIAL')
        print('11 - ENCERRAR PROGRAMA')
        print('--------------------------')
        opc, result = 0,0
        try:
            opc=int(input('Digite o numero da sua opção: '))
            if opc==8:
                break
            if opc > 0 and opc < 8:
                a=int(input('a: '))
                b=int(input('b: '))
            if opc > 7 and opc < 12:
                a=int(input('a: '))     # CALCULOS COM UM NUMERO
            if opc==1:
                resul=soma(a,b)
            if opc==2:
                resul=subtracao(a,b)
            if opc==3:
                resul=multiplicacao(a,b)
            if opc==4:
                resul=divisao_real(a,b)
            if opc==5:
                resul=divisao_inteira(a,b)
            if opc==6:
                resul=resto_divisao(a,b)
            if opc==7:
                resul=potencia(a,b)
            if opc==8:
                resul=fatorial(a)
        except:
            print('Opção inválida... Tente novamente')
            print('--------------------------')
            opc=10
        if opc > 0 and opc < 8:
            print('A resposta é: ',resul)
            while True:
                try:
                    opc=int(input('Digite 0 para sair ou qualquer outro numero para continuar: '))
                    break
                except:
                    print('Você não digitou um numero.')
            if opc==0:
                break        
exit()
