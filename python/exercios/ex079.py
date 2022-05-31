lista=[]
for c in range (0,5):
    lista.append(int(input(f'Digite o valor da posição {c} :  ')))
maior=max(lista)
menor=min(lista)
print(f'Os valores digitados foram {lista}')
print (f'o maior numero digitado foi {maior} e foi digitado na posição ',end='')
for  pos ,c in enumerate(lista) :
    if maior ==c:
        print (f'{pos}...')
print(f'O menor valor digitado foi {menor} e foi digitado na posição ' , end='')
for pos , m in enumerate (lista):
    if menor==m:
        print(f'{pos}...',end='')
