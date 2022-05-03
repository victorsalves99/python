
contador= n= s =0
n=int(input('Digite um numero [Digite 999 para parar ]:'))
while n!=999:
    contador+=1
    s+=n
    n=int(input('Digite um numero [Digite 999 para parar ]:'))
print('A quantidade de numeros foi {} e a soma entre eles é {} '.format(contador, s ))
