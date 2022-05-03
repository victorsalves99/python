import time
import random
print('''Escolha uma das opções
[0]PEDRA
[1]PAPEL
[2]TESOURA ''')
jogador=int(input('qual a sua escolha ? '))
itens=( 'PEDRA' ,'PAPEL' ,'TESOURA') # criou uma lista com posiçoes 0 ,1 ,2 
computador=random.randint(0,2)#o computador escolheu um numero entre 0,2 
print('O computador escolheu {} '.format(itens[computador]))# ta dizendo para que nos itens escolha o nome que esta na posiçao em que o computador escolheu 
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!')
if computador==0 :
    if jogador==0:
        print('\033[1;34;40m EMPATE\033[m')
    elif jogador==1:
        print('\033[1;32;40m JOGADOR GANHOU \033[m')
    elif jogador==2:
        print('\033[1;31;40m COMPUTADOR GANHOU \033[m')
    else:
        print('invalido ')

elif computador== 1 :
    if jogador==0:
        print('\033[1;31;40m COMPUTADOR GANHOU \033[m')
    elif jogador==1:
        print('\033[1;32;40m EMPATE \033[m')
    elif jogador==2:
        print('\033[1;34;40m JOGADOR GANHOU \033[m')
    else:
        print('invalido ')
elif computador==2:
    if jogador==0:
        print('\033[1;32;40m JOGAODR GANHOU\033[m')
    elif jogador==1:
        print('\033[1;31;40m COMPUTADOR GANHOU \033[m')
    elif jogador==2:
        print('\033[1;34;40m EMPATE \033[m')
    else:
        print('invalido ')

    







