maior=0
menor=0
for c in range(1,6):
    peso=float(input('digite o peso da {} pessoa ' .format(c)))
    if c==1:
        maior=peso
        menor=peso
    else:
        if maior<peso:
            maior=peso
        if peso<menor:
            menor=peso
print('o maior peso foi {} KM'.format(maior))
print('O menor pesso foi {} KM '.format(menor))


        
        