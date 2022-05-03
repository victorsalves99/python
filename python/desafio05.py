                                     #tuplas 



lanche=('haburger','pizza', 'suco', 'pudim')
print(lanche)
print(lanche [2]) # Ele vai mostrar o lanche na possição dois 
print(lanche[1:3]) # Ele vai mostrar da pasição um até a pasição dois pois a ultima possição é descartada 
print(lanche[1:]) # Ele vai mostrar do lanche na possição um ate a ultima passição 
print(lanche [:2]) #Ele vai mostra  da possição inicial até a possição um pois a ultima é  sempre iguinorada  
print(lanche[-3:]) #Ele vai conta da ultima posição ate o final ou seja -1 é igual a 3 nesse exemplo 
#lanche[1]= cuscuz #Ele nao funciona pq as tuplas sao imutaveis 
for comida in lanche:
    print(f'Vou comer {comida}')
print('comi de mais' )
for cont in range(0,len(lanche)):
    print(f'vou comer {lanche[cont]}')
for pos, cont in enumerate(lanche): # a primeira variavel recebe a possição e a segunda recebe o nome do elemento 
    print(f'vou comer {cont} na possição {pos}')
a=(1,2,3,4)
b=(5,6,7)
c=a+b
print(c.count(3)) #vai contar quantas vezes tem o numero 3 
print(c.index(5)) #vai mostrar em qual possição esta o numero 
