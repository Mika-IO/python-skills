print()

#1

def segundos(h,m,s):
    s = (h*60*60) + (m*60) + s
    return s 
segundos=segundos(3,23,17)
print('3 horas, 23 minutos e 17 segundos tem ',segundos,'segundos')
print('------------------------------------------------------------------------------------------------')

#2

def metros(km):
    metros=km*1000
    return metros
def velocidadeMedia(m,s):
    v=m/s
    return v

print('Se você correr 63km em 3hrs 23min e 17seg sua velocidade média em m/s é: ',velocidadeMedia(metros(63),segundos))
print('------------------------------------------------------------------------------------------------')

#3

print('(100 − 413 · (20 − 5 × 4)) / 5 é igual á ',(100 - 413 * (20 - 5 * 4)) / 5)
print('------------------------------------------------------------------------------------------------')

#4

c1,c2,c3 = 10,22,6.8
crP=c1+c2+c3
crS=1/(1/c1+1/c2+1/c3)
print('Capacitor 1: ',c1,' Capacitor 2: ',c2,' Capacitor 3:', c3)
print('Em paralelo sua capacidade resultante total é: ',  crP)
print('Em serie sua capacidade resultante total é: ', crS)
print('------------------------------------------------------------------------------------------------')

#5

def compraKilo(precoKilo,pesoGramas):
    preco = (precoKilo/1000) * pesoGramas
    return preco

compra = 75*2.2 + 2*8.73 + 3.45 + compraKilo(5.4,420) + compraKilo(30,250) + compraKilo(25,450)
print('O valor que cada um vai pagar na compra é: ',compra/4,' reais.')
print('------------------------------------------------------------------------------------------------') 

# 6
# ESSE EXERCICIO MERECE ATÉ UM COMENTARIO ESSE EXERCICIO... O CARA QUE ECREVEU ESSA PORRA É UM GÊNIO KKKKKKK

from math import pi
volumePote = 15*10*13
raioDaBolinhaDeQueijoKKKKKKKKKK = 1.2
volumeBolinhaDeQueijoKKKKKKKKKK =   (4/3)*pi*raioDaBolinhaDeQueijoKKKKKKKKKK
volumePreenchidoPelasBolinhasDeQueijoNoPoteKKKKKKKKKK = volumePote - ((volumePote/100)*74)
numeroDeBolinhasDeQueijoQuemCabemNoPote = volumePreenchidoPelasBolinhasDeQueijoNoPoteKKKKKKKKKK / volumeBolinhaDeQueijoKKKKKKKKKK
numeroDeBolinhasDeQueijoQuemCabemNoPote = int(numeroDeBolinhasDeQueijoQuemCabemNoPote)
print('Cabem ',numeroDeBolinhasDeQueijoQuemCabemNoPote,' bolinhas de queijo no pote KKKKKKKKKK')
print('------------------------------------------------------------------------------------------------')
