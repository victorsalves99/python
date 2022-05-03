
n=int(input('Digite um numero : '))
resp=str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
cont =1
soma=n
menor=n
maior=n
resp='S'
while resp!='N':
    n=int(input('Digite um numero : '))
    cont+=1
    soma=soma+n
    if  n > maior:
        maior=n
    if n < menor:
        menor=n
    resp=str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
media = soma /cont
print('O total de numeros digitados foram {} e a media entre eles é de {:.2f} '.format(cont,media ))
print('O maior numero foi {} e o menor numero foi {} '.format(maior,menor))


    