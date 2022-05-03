print('-='*20)
n1=int(input('escolha um numero '))
n2=int(input('escolha outro numero '))
print('-='*20)

if n1<n2:
    maior=n2
    menor=n1
    print('o maior valor é {} e o menor valor é {} '.format(maior,menor))
elif n2<n1:
    maior=n1
    menor=n2
    print('o maior valor é {} e o menor valor é {} '.format(maior,menor))
    
else:
    print('Os dois valores são iguais ')