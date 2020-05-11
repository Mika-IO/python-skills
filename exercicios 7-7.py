print()

#1

dolar = 3.25
print('65 reais valem',65/dolar)
print('------------------------------------------------------------------------------------------------')

#2

def mA(a,b,c,d):
    media = (a+b+c+d)/4
    return media
def mG(a,b,c,d):
    from math import sqrt
    media = sqrt(a*b*c*d)
    return media
def mH(a,b,c,d):
    media = 4/(a+b+c+d)
    return media
a,b,c,d = 8.66,5.35,5,1
m1,m2,m3 = mA(a,b,c,d),mG(a,b,c,d),mH(a,b,c,d)
print('A média aritmédica é: ',m1,' A média geométrica é: ',m2,' E a média harmonica é: ',m3)
if m1 > m2 and m1 >m3:
    print('O professor fdp vai usar média aritmética esse pau no cú')
if m2 > m1 and m2 > m3:
    print('O professor arrombado vai usar média geométrica')
if m3 > m1 and m3 > m2:
    print('Esse professor fudido vai usar média harmonica')
print('------------------------------------------------------------------------------------------------')

#3 

compra = 299.99 + 23.87 + 66.66 + 6 * 1.42 + 12.34
iof = (compra/100)*6.38
compra = compra * dolar + iof
print('O valor total da compra é ',compra,' sendo que ',iof,' reais são de IOF')
print('------------------------------------------------------------------------------------------------')
