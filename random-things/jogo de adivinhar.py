from random import randint

print("""
    #########################################
    ########## JOGO DA ADIVINHAÇÃO ##########
    #########################################
""")


continuar = True
while continuar:    
    numero = randint(0,101)

    print(numero)
   
    print("""

ADIVINHE O NUMERO DE 0 A 100!!! VOCÊ TEM 10 TENTATIVAS

        """)
   
    acertou,tentativas = False,0
    while (not acertou and tentativas < 10):
    
        tentativas += 1
        print()
        
        chute = int(input('Chute: '))
        acertou = chute==numero
        maior = chute>numero
        menor = chute<numero
        
        if(acertou):
            print('ACERTOU!!')
            print()
            continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
    
        elif(maior):
            print(f'Chute foi maior que o numero sorteado!!! Você tem {10 - tentativas}tentativas!!!') 
            if tentativas == 10:
                print('GAME OVER!!')
    
        elif(menor):  
            print(f'Chute foi menor que o numero sorteado!!! Você tem {10 - tentativas} tentativas!!!') 
            if tentativas == 10:
                print('GAME OVER!!')
                print()
                continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
