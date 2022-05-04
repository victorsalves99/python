listagem=('lapis',3,'boraacha',5,'caneta',1,'tesoura',6)
print('-'*35)
print(f'{"LISTAGEM DE PRODUTOS ":^30}')
print('-'*35)

for item in range(0,len(listagem)):
    if item%2==0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'{listagem[item]:>5.2f}')

print('-'*35)
    