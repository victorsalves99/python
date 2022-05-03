primeirotermo =int(input('Digite o primeiro termo '))
rasao = int (input('Digite a rasão '))
termofinal=primeirotermo
cont=1
quantidadetermo=0
mais=10

while mais!=0:
    
    quantidadetermo+=mais
    while cont<=quantidadetermo:
        print('{}'.format(termofinal),end='')
        print('>>' if cont<quantidadetermo else ' pause',end='')
        termofinal+=rasao
        cont+=1
    print(end='\n')
    mais=int(input('Quer ir mais quanto?'))
    
print('Progreção finalizada com {} temos mostrados !'.format(quantidadetermo))

   




