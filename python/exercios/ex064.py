print('-='*20)
termos=int(input('Quantos termos voce quer ver? '))
print('-='*20)
cont=3
n1=0
n2=1
alxiliar=0
print('{} -> '.format(n1),end='')
print('{} -> '.format(n2),end='')
while cont<=termos:
    alxiliar=n1+n2        
    print('{} -> '.format(alxiliar),end='')
    n1=n2
    n2=alxiliar
    cont+=1
print('FIM')
        



