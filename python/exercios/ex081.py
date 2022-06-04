lista=[]
for c in range(0,5):
    num=int(input('Digite um valor : '))
    if c==0:
        lista.append(num)
        print('Valor adicionado no final da lista ')
    elif num > lista[-1]:
        lista.append(num)
        print('Valor adicionado no final da lista ')
    else :
        pos=0
        while pos < len(lista):
            if num < lista[pos]:
                lista.insert(pos,num)
                print(f'valor adicionado na posição {pos}')
                break
            pos=pos+1

                
    
print(f'os valores da lista é {lista}')
