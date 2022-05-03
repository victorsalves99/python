import math
an=float(input('qual o angulo voce deseja ? '))
angulo=math.radians(an)
seno= math.sin(angulo)
tangente= math.tan(angulo)
coseno=math.cos(angulo)
print('o seno de {:.0f} é {:.2f} '.format(an,seno))
print('o coseno de {} é {:.2f} '.format(an,coseno))
print('a tangente de {} é {:.2f} '.format(an,tangente))
