velocidade=int(input('qual a velocidade do carro ? '))
if velocidade<= 80 :
    print ('Tenha um boa viagem dirija com cuidado')
else:
    multa=(velocidade-80)*7
    print('VOCÊ EXEDEU O LIMITE DE VELOCIDADE DE 80 KM/H')
    print('SUA MULTA É DE R${} '.format(multa))
