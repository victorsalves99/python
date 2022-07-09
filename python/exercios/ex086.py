lista=[[],[]]
for c in range(0,7):
    num=int(input(f'digite o {c} valor: '))
    if num%2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('=-'*30)
print(f'os valores pares digitados foram : {lista[0]}')
print(f'os valores impares digitados foram : {lista[1]}')
