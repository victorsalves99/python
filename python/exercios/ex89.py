import random
from time import sleep
quina=[]
c=0
cont=0

print('-'*60)
print(f"{'QUER SEU PALPITE PARA QUINA DE SÂO JOÃO':*^60}")
print('-'*60)
res=str(input(''))[0]
while res!='n'or res!='N':
    palpite=int(input('Quantos palpites você quer? : '))
    print('-'*60)
    print(f"{'SEUS PALPITES SÃO':*^60}")
    print('-'*60)
    while cont<palpite:
        while len(quina)!=5:
            numero=random.randint(1,60)
            if numero not in quina:
                quina.append(numero)
        quina.sort()
        sleep(1)
        print(f'{quina}')
        quina.clear()
        cont+=1
    res=str(input('Quer continuar : S/N '))[0]
    cont=0
    if res in 'nN':
        break
print('-='*30)
print(f"{'BOA SORTE VOLTE SEMPRE':*^60}")
print('-='*30)
    