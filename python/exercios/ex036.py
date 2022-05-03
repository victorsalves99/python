print('-='*20)
print('Olá seja bem vindo ! ')
print('vamos ver uma casa pra voce ')
print('-='*20)
valorcasa=float(input('qual o valor da casa ? '))
salario=float(input('qual o su salario ? '))
anos=int(input('em quntos anos voce quer dividir ? '))
meses= anos*12
valorparcela=valorcasa/meses
porcentagemsalario=salario*30/100
if porcentagemsalario>=valorparcela:
    print('\033[0;34;43m PARABENS! \033[m, foi foi aprovado para comprar a casa !')
    print('Sera {} parcelas de R${:.2f} !'.format(meses,valorparcela))
else:
    print('Sera {} parcelas de R${:.2f} !'.format(meses,valorparcela))
    print('\033[0;31;43m SINTO MUITO !\033[m Voce nao esta apto para compra esta casa ')

