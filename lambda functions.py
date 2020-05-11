print("""

      ------ lambda functions ------

""")

print('Soma em lambda:',(lambda x,y: x + y)(10,15))

ao_quadrado_lambda = lambda x: x**2 

def ao_quadrado_convencional(x):
    return x**2

print('Função ao quadrado lambda:',ao_quadrado_lambda(5))
print('Função ao quadrado convencional:',ao_quadrado_convencional(5))

from math import log

log10 = lambda a: log(a,10)     #HIGH ORDEN LAMBDA FUNCTION

print('Log de 100 na base 10 em lambda:',log10(100))

# TABELA VERDADE COM LAMBDA FUNCTIONS
NOT = lambda a: not a

OR = lambda a, b: True if a==1 or b==1 else False

NOR = lambda a, b: not (OR(a,b))

AND = lambda a, b: True if a==1 and b==1 else False

NAND = lambda a, b: not (AND(a,b))

XOR = lambda a, b: True if a != b else False

XNOR = lambda a, b: not (XOR(a, b))

print()
print('TABELA VERDADE!!')

print('NOT 1:',NOT(1))
print('NOT 0:',NOT(0))

tupla_possibilidades = (0,0,1,1,1,0,0,1)
ind1,ind2 = 0,1

for i in range(4):
    a,b = tupla_possibilidades[ind1],tupla_possibilidades[ind2]
    ind1,ind2 = ind1+1,ind2+1
    print(f'OR    {a} {b}:',OR(a,b))
    print(f'NOR   {a} {b}:',NOR(a,b))
    print(f'AND   {a} {b}:',AND(a,b))
    print(f'NAND  {a} {b}:',NAND(a,b))
    print(f'XOR   {a} {b}:',XOR(a,b))
    print(f'XNOR  {a} {b}:',XNOR(a,b))
