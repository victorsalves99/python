from time import sleep
def contar(a,b,c):
    if a<b and c>0:
        print('-='*30)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a,b+1,c):
            print(f'{c}',end=' ' ,flush=True)
            sleep(0.5)
        print(f'fim')
        print('-='*30)
    elif a>b and c>0:
        print('-='*30)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a,b-1,-c):
            print(f'{c}',end=' ' ,flush=True)
            sleep(0.5)
        print(f'fim')
        print('-='*30)
    elif a>b and c<0:
        print('-='*30)
        print(f'Contagem de {a} até {b} de {c} em {c}')
        for c in range(a,b-1,c):
            print(f'{c}',end=' ' ,flush=True)
            sleep(0.5)
        print(f'fim')
        print('-='*30)

contar(1,10,1)
contar(10,0,2)
contar(int(input(f'inicio: ')),int(input('fim: ')),int(input('passos: ')))
