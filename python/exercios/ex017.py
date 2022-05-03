from math import hypot
co=float(input('qual o cateteto oposto ? '))
ca=float(input('qual o cateto adjasente ? '))
hi=hypot(co,ca)
print('a hipotenusa é {:.2f}'.format(hi))


import math
catetooposto=float(input('digite o cateto oposto '))
catetoadjacente=float(input('digite p cateto adjacente '))
hipotenusa=math.hypot(catetooposto,catetoadjacente)
print('a hipotenusa é {:.2f}'.format(hipotenusa))
