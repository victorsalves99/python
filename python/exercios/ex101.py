from random import randint
pares=[]
numeros=[]
def sorteio ():
    print(f'Sorteado 5 valores da lista',end=' ',flush=True)
    for c in range(0,5):
        num=randint(0,9)
        print(f'{num}',end=' ')
        if num%2==0:
            pares.append(num)
            numeros.append(num)
        else:
            numeros.append(num)
            
    print(f'Pronto')
def soma (list):
    print(f'somando os valores pares de {numeros} temos :{sum(list)}')



sorteio()
soma(pares)