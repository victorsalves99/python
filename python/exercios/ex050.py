soma=0
cont=0
for c in range(1,7):
    num=int(input('Diigite o valor '))
    if num%2==0:
        soma=soma+num
        cont+=1
print('fora digitados {} numeors pares e a soma entre eles  é {}'.format(cont,soma))