from time import sleep
def analise(*num):
    print('-='*30)
    print(f'Analisando valores : ')
    for c in num:
        print(f'{c}',end=' ',flush=True)
        sleep(0)
    print(f'Foram informados {len(num)} valores. ')
    print(f'O maior valor informado foi {max(num)}')


analise(3,4,5,6,7)
analise(2,44,24,32)
analise(3,6,4)
analise(9,3)
analise(5,7)



