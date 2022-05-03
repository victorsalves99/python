maiorhomen=0
maiormulher=0
menorhomem=0
menormulher=0
for c in range(0,7):
    
    sexo = str (input('Qual o seu sexo ? ')).strip().upper()
    idade= int (input('Qual a sua idade ? '))
    if idade >=18 and sexo=='M' :
        maiorhomen +=1
    elif idade >=18 and sexo == 'F':
        maiormulher+=1
    elif idade < 18 and sexo =='M':
        menorhomem+=1
    elif idade < 18 and sexo == 'F':
        menormulher+=1
print('O total de pessoas maiores de idade é {} e {} delas sao mulheres e {} sao homens '.format(maiorhomen+maiormulher,maiormulher,maiorhomen))
print('Sao menores {} pessoas sendo {} delas mulheres e {} homens '.format(menorhomem+menormulher,menormulher,menorhomem)
)
    