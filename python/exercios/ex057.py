
idadevelho=0
media=0
menosde20=0
for c in range(1,6):    
    print('-'*20)
    print('{} pessoa '.format(c))
    nome=str(input('Digite o nome '))
    idade = int(input('Idade '))
    sexo = str(input('[F/M]')).strip().upper()
    media=media+idade
    mediafinal=media/5
    if sexo=='F' and idade<20:
        menosde20=menosde20+1
    elif sexo=='M':
        if idade>idadevelho:
            idadevelho=idade
            nomevelho=nome
    



print('A media de idade desse grupo é de {}'.format(mediafinal))
print('O homem mais velho foi {} com a idade de {} anos'.format(nomevelho,idadevelho))
print('Existem no total {} mulheres abaixo dos 20 anos '.format(menosde20))

    


