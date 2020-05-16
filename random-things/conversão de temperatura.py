def fahrenheit_pra_celsius(f):
    c = ((f-32)/9)*5
    return c

def celsius_pra_fahrenheit(c):
    f = ((c/5)*9)+32 
    return f

print('\n##### CONVERSOR DE TEMPERATURAS #####\n')
while True:
    try:
        n = int(input('Digite a temperatura: '))
        print
        print(n,' Celsius é ',celsius_pra_fahrenheit(n),' Fahenheit. ')
        print(n,' Fahenheit é ',fahrenheit_pra_celsius(n),' Celsius. ')
        print()
    except:
        print('Você fez algo errado. A temperatura é um numeral man...')
