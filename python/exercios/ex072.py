print(('-='*20))
print('{:-^40}'.format('Caixa Eletronico '))
print(('-='*20))
sacar=float(input('Quanto quer sacar ? : R$'))
if sacar>=50:
    nota50=sacar/50
    sacar=sacar%50
    if nota50>1:
        print(f'{nota50:.0f} CEDULAS DE R$50')
    else:
        print(f'{nota50:.0f} CEDULA DE R$50')
if sacar<50 and sacar >=20:
    nota20=sacar/20
    sacar=sacar%20
    if nota20>1:
        print(f'{nota20:.0f} CEDULAS DE R$20')
    else:
        print(f'{nota20:.0f} CEDULA DE R$20')
if sacar<20 and sacar >=10:
    nota10=sacar/10
    sacar=sacar%10
    if nota10>1:
        print(f'{nota10:.0f} CEDULAS DE R$10')
    else:
        print(f'{nota10:.0f} CEDULA DE R$10')
if sacar<10 and sacar >=5:
    nota5=sacar/5
    sacar=sacar%5
    if nota5>1:
        print(f'{nota5:.0f} CEDULAS DE R$5')
    else:
        print(f'{nota5:.0f} CEDULA DE R$5')

if sacar<5 and sacar >=1:
    nota1=sacar/1
    if nota1>1:
        print(f'{nota1:.0f} CEDULAS DE R$1')
    else:
        print(f'{nota1:.0f} CEDULA DE R$1')

