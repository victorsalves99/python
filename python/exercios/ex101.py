from random import randint
from time import sleep
pares=[]
numeros=[]
def sorteio ():
    print(f'Sorteado 5 valores da lista',end=' ')
    for c in range(0,5):
        num=randint(0,9)
        sleep(0.8)
        print(f'{num}',end=' ',flush=True)
        if num%2==0:
            pares.append(num)
            numeros.append(num)
        else:
            numeros.append(num)
            
    print(f'Pronto!')
def soma (list):
    print(f'somando os valores pares de {numeros} temos :{sum(list)}')


print('-='*30)
sorteio()
print('-='*30)
soma(pares)
print('-='*30)
