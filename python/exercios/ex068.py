
while True:
    cont=0
    print('-='*20)
    n=int(input('Digite o valor que quer saber a taboada : '))
    if n<0:
        break
    while cont <=10:
        print('{:2} X {:2} = {:2}'.format(n,cont,cont*n))
        cont+=1
print('Fim do programa ')