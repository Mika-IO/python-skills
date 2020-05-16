import random

frutas = ['Banana','Melancia','Pera','Ameixa','Laranja']
favorita = random.choice(frutas).upper()
palpite, tentativas = '',0

while favorita != palpite:
    tentativas += 1
    i=1 
    print(f'{frutas}\n')
    palpite=input('Qual fruta é minha favorita? ')
    palpite=palpite.upper()
    if favorita != palpite:
        print('Você errou... tente de novo')
        print()

print('Você acertou com ',tentativas,' tentativas... Parabéns!!!\n')
