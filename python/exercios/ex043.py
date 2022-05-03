nome=str(input('qual o seu nome ? '))
print('ola {} vamos ver seu IMC '.format(nome))
altura=float(input('diga a sua altura '))
peso = float(input('diga o seu peso '))
imc=peso/(altura*altura)
if imc <18.5:
    peso2='A BAIXO DO PESO '
elif 18.5<=imc<=25:
    peso2='NO PESO IDEAL '
elif 25< imc <=30 :
    peso2='COM SOBREPESO'
elif 30<imc<=40:
    peso2='COM OBESIDADE '
else:
    peso2='COM OBESIDADE MORBIDA '



print('O indece de massa corporal IMC  é {:.2f} voce esta {} '.format(imc,peso2))
