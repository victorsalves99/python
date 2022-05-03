import random
vitoria=0
while True:
    print('-='*30)
    print('VAMOS JOGAR PAR OU IMPAR ')
    print('-='*30)
    computador = random.randint(1,5)
    print('''
    PAR
    IMPAR ''')
    escolha=str(input('Faça sua escolha ')).strip().upper()[0]
    jogador = int(input('Escola um numero :'))
    soma=computador+jogador
    print(f'O computador colocu {computador} e voce colocou {jogador} e a soma é {soma} ')
    if escolha=='P':
        if soma%2==0:
            print('Jogador Ganhou')
            vitoria+=1
        else:
            print('Computador Ganhou ')
            break
    elif escolha=='I':
        if soma%2!=0:
            print('Jogador Ganhou ')
            vitoria+=1
        else:
            print('Computador Ganhou ')
            break
print(f'GAME OVER ! VOÇÊ GANHOU {vitoria} VEZES')




