numero=(int(input('Digite um numero ')),int(input('Digite um numero ')),int(input('Digite um numero ')),int(input('Digite um numero ')))
print(f'os numeros digitados fora, {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes ')
if 3 in numero : #quer dizer que se o numero 3 estiver dentro da varialvel numero ele vai rodar 
    print(f'O valor 3 aparece na posição {numero.index(3)+1}')
else:
    print(f'O valor 3 nao aparece !')
print(f'Os valores pares digitados foram :',end=" ")
for n in numero:
    if n%2==0:
        print(n,end=" ")
