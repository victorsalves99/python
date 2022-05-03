s=cont=0
while True :
    n=int(input('Digite um numero [999 para parar ]'))
    if n==999:
        break
    s+=n
    cont+=1
media=s/cont
print(f'Foram digitados {cont} e a media entre eles é de {media} ')