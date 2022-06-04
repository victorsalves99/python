lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    res=str(input('Quer continuar ? [S/N]')).upper().strip()
    if res=='N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print(f'O valores da lista são {lista}')
if 5 in lista:
    print(f'O valor 5 está presente !')
else:
    print(f'O valor 5 não está presente !')


