lista=[]
while True :
    
    num=int(input('Digite um valor :  '))
    
    
    if num not in lista:
        lista.append(num)
        print(f'Valor adicionado com sucesso !')
    else :
        print(f'Valor já existente ')
    resp=str(input('Quer continuar : [S/N]' )).upper()
    if resp == 'N':
            break
lista.sort()
print(f'os valores digitados foram esses {(lista)}')
    