import random
import time # é a biblicoteca de tempo
lista=[0,1,2,3,4,5]
escolha=random.choice(lista)#choice é pra escolher um numero dentro de uma lista 
print('-------=-----------=-----------=-------')
print('vou pensar em um numero tente advinhar ')
print('-------=-----------=-----------=-------')
escolhido=int(input('escolha um numero entre 0 e 5! '))
print('PROCESSANDO ...')
time.sleep(3)#esse o computador ira esperar 3 segundos pra mostrar 0 resultado na tela 
if escolhido==escolha:
    print('O numero que eu escolhi foi {} '.format(escolha))
    print('PARABENS! você venceu ')
else:
    print('O numero que eu escolhi foi {}'.format(escolha))
    print('a maquna venceu ')
