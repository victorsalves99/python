import datetime
nome=str(input('qual o seu nome ? '))
nasc=int(input('qual ano voce nasceu ? '))
anos=datetime.date.today().year - nasc
if anos <=9:
    print('olá {} ! voce tem {} e é um atleta mirim '.format(nome,anos))
elif 14>=anos>9:
    print('olá {} ! voce tem {} e é um atleta infantil '.format(nome,anos))
elif 19>=anos>14:
    print('olá {} ! voce tem {} e é um atleta junior '.format(nome,anos))
elif 25>=anos>19 :
    print('olá {} ! voce tem {} e é um atleta senior '.format(nome,anos))
else:
    print('olá {} ! voce tem {} e é um atleta master '.format(nome,anos))
