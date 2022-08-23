import datetime

def verificar(i=0):
    if idade <18 and idade>=16 or idade>65:
        return print(f'voto opcional')
    elif idade>=18 and idade<=60:
        return print(f'Voto Obrigatorio')
    else:
        return print(f'Voce não vota!')


anoatual=datetime.date.today().year
anoNacimento = int(input('Em que ano voce nasceu ?  :'))
idade= anoatual-anoNacimento

print(f'Você tem {idade} anos de idade')
verificar(idade)