print('-='*20)
print('PA')
print('-='*20)
termo=int(input('Digite o terno :'))
rasao=int(input('Digite a rasao :'))
decimo=termo
cont=1
while cont<=10:
    print('{}'.format(decimo),end='')
    print(' >> 'if cont<10 else'.',end='')
    decimo=decimo+rasao
    cont+=1
print('FIM')



