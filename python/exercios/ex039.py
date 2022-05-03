import datetime
nasc=int(input('qual ano voce nasceu? '))
ano=datetime.date.today().year
idade=ano-nasc



if idade>18:
    print('precisa se alistar ')
    print('você ja passou da tada de alistamento a {} anos'.format(ano-(nasc+18)))
elif idade<18:
    print('Nao precisa se alistar ainda')
    print('so presisara se alista daqui a {} anos '.format((nasc+18)-ano))
else:
    print('esta na idade certa pra se alistar ')