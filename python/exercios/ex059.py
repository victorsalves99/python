import random
computador=random.randint(0,10)
print('Adivinhe o numero no qual o computador escolheu ')
print('Escolha um numero de 1 a 10 ')
jogador = int(input('seu palpite '))
palpites =1 
print(computador)
print(jogador)
while computador!=jogador:
    if computador==jogador: 
        palpites+=1
    elif computador>jogador:
        print('Errou ! Tente novamente , dica é mais ')
        jogador = int(input('seu palpite '))
        palpites+=1
    else:
        print('Errou ! Tente novamente , dica é menos ')
        jogador = int(input('seu palpite '))
        palpites+=1
print('Acertou ! foram ultilizadas {} tentativas '.format(palpites))


