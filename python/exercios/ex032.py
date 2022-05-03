import time
import datetime
ano=int(input('digite um ano qualquer ou coloque 0 para analisar o ano atual '))
print('ANALISANDO ...')
time.sleep(2)
if ano==0:
    ano=datetime.date.today().year #para usar a data do seu computador 
if ano%4==0 and ano%100!=0 or ano%400==0 :
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} nao é bisexto'.format(ano))
