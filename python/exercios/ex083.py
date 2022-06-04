lista=[]
pares=[]
impares=[]
while True:
    lista.append(int(input('Digite um valor : ')))
    res=str(input('Quer continuar : [S/N]'))
    if res in 'Nn':
        break
lista.sort()
for c in lista:
    if c%2==0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Os valores da lista são {lista}')
print(f'Os valores da lista que são pares sao{pares}')
print(f'Os valores da lista que são impares sao{impares}')



