
from random import randint
from time import sleep
from operator import itemgetter
jogador={
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6),
}
print(f'valores sorteados ')
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking=[]
ranking=sorted(jogador.items(),key=itemgetter(1), reverse=True)
print(f'-='*20)
print(f'  == RANKING DOS JOGADORES == ')
for a,b in enumerate(ranking):
    print(f'{a+1} lugar : {b[0]} que tirou {b[1]}')
    


        
    




