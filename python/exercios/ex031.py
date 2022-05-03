distacia= float(input('qual a distancia da sua viagem ? '))
if distacia<=200:
    valor=distacia*0.50
    print('O valor a ser pago para a distacia de {:.2f}KM é R${:.2f}'.format(distacia,valor))
else:
    valor=distacia*0.45
    print('O valor a ser pago para a distancia de {:.2f} KM é R${:.2f}'.format(distacia,valor))
print('Obrigado! Tenha uma boa viagem !')
