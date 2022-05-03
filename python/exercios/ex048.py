soma=0
cont=0
for c in range(1, 500+1,2):
    if c%3==0:
        soma=soma+c
        cont=cont+1
print('a quantidade de numeros impar divisiveis por 3 é {} e a soma é {}'.format(cont,soma))




