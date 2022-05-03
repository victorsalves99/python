import random
import time #impotar o contre de tempo
print('''Escola pedra , papel ou tesoura 
[1]PEDRA
[2]PAPEL
[3]TESOURA''')
resposta=int(input(''))
lista=[1,2,3]
maquina=random.choice(lista)

print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!')
if maquina==resposta:
    if maquina==1:
        print('Os dois esxolheram pedra ! NINGUEM GANHOU  ')
    elif maquina==2:
        print('Os dois escolheram papel ! NINGUEM GANHOU  ')
    elif maquina==3:
        print('Os dois escolheram tesoura ! NINGUEM GANHOU  ')
elif maquina==1 and resposta==2 or maquina==2 and resposta==1:
    if maquina<resposta:
        print('''A maquina escolheu PEDRA 
voce escolheu PAPEL ! 
VOCÊ VENCEU   ''')
    elif maquina>resposta:
        print('''A maquina escolheu PAPEL!
voce escolheu PEDRA ! 
A MAQUINA VENCEU  ''')
elif maquina==2 and resposta==3 or maquina==3 and resposta==2:
    if maquina<resposta:
        print(''' A maquina escolheu PAPEL !
voce escolheu TESOURA !
VOCE VENCEU ''')
    elif maquina>resposta:
        print('''A maquina escolheu TESOURA !
voce escolheu PAPEL ! 
A MAQUINA VENCEU ''')
elif maquina==3 and resposta==1 or maquina==1 and resposta==3:
    if maquina>resposta:
        print('''A maquina escolheu TESOURA!
voce escolheu PEDRA !
VOCE VENCEU ''')
    elif maquina<resposta:
        print('''A maquina escolheu PEDRA !
voce escolheu TESOURA
A MAQUINA VENCEU ''')
else:
    print('VOCE NAO ESCOLHEU NEM UMA OPÇÃO ')







