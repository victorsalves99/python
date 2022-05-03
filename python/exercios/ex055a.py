import datetime
anoatual=datetime.date.today().year
maior=0
menor=0
for c in range(1,8):
    nascimento=int(input('digite o ano de nascimendo da pessoa {} :'.format(c)))
    idade=anoatual-nascimento
    if idade >=18:
        maior=maior+1 
    elif idade <18:
        menor=menor+1
print('''existem {} pesooas maiores e 
Existem {} pessoas menores '''.format(maior ,menor))


