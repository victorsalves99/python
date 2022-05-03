import random
from struct import unpack
computador= random.randint(0,5)#radiente e pra fazer ele escolher um numero entre o 0, 5 nesse caso 
print(computador)
resp=int(input('escolha um numero '))
if resp==computador:
    print('voce acertou ')
else:
    print('voce errou ')