def args(arg1,*args):
    print()
    print(f'Argumento1: {arg1}')
    n = 0
    for arg in args:
        n += 1
        print(f'Argumento{n+1}: {arg}')
    print()

args('m','i','k','a','i','o')
args(1,2,3,4,5)

nome = list('MIKAIO')

args(*nome)

def kwargs_key_and_value(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} = {value}')

pessoa1 = {'nome':'Mikaio','idade':17}
pessoa2 = {'nome':'Joazin','idade':9}
pessoa3 = {'nome':'Sherek','idade':170}
pessoa4 = {'nome':'Leticia','idade':17}
pessoas = [pessoa1,pessoa2,pessoa3,pessoa4]

for pessoa in pessoas:
    kwargs_key_and_value(**pessoa)
    print()

def teste_args_kwargs(arg1, arg2, arg3):
    print()
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    print(f'arg3: {arg3}')

args = (1,2,3)
kwargs = dict(arg1 = 1, arg2 = 2, arg3 = 3)
teste_args_kwargs(*args)
teste_args_kwargs(**kwargs)
print()
