print('-='*20)
print('analisandor de triangulo ')
print('-='*20)
r1=float(input('primeira reta '))
r2=float(input('segunda reta '))
r3=float(input ( 'terceira reta '))
if r1==r2 ==r3 :
    tipo='\033[1;31;40mEQUILATERO\033[m'
elif r1==r2!= r3 or r1==r3!=r2 or r3==r2!=r1:
    tipo='\033[1;34;40mISOCELES\033[m'
else:
    tipo = '\033[1;31;40mESCALENO\033[m'

if r1<r2+r3 and r2<r1+r3 and r3< r1+r2:
    print('é possivel formar o triangulo {} '.format(tipo))
else:
    print('nao é possivel formar o triangulo ')