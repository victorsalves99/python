ficha=[]
while True:
    nome=str(input('Nome:'))
    nota1=float(input('nota 1:'))
    nota2=float(input('nota 2:'))
    meida=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],meida])
    cont=str(input('Quer continuar ?:[s/n]'))
    if cont in 'nN':
        break
    
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>10} ')
print('-'*30)
for pos,c in enumerate(ficha):
    print(f'{pos:<4}{ficha[pos][0]:<10}{ficha[pos][2]:>10}')
print('-'*30)
resp=0
while True:
    resp=int(input('Mostrar a nota de qual aluno ? :digite 999 pra interromper:  '))
    if resp==999:
        break
    print(f'As notas de {ficha[resp][0]} são {ficha[resp][1]}')
    
    


            
                



