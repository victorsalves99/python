homemmaior=0
homemmenor=0
mulhermaior=0
mulhermenor=0
invalidos=0
for p in range (0,7):
    
    nome=str(input('qual seu nome ? '))
    sexo=str(input('qual seu sexo ? ')).lower()
    ano=int(input ('wual ano voce nasceu ? '))
    idade= 2022-ano

    if sexo=='m' and idade>=18:
        homemmaior+=1
    elif sexo=='f' and idade>=18:
        mulhermaior+=1
    elif sexo=='m' and idade<18:
        homemmenor+=1
    elif sexo=='f' and idade<18:
        mulhermenor+=1
    else:
        invalidos+=1
print('existem {} pessoas maiores sendo {} mulheres e {} homens'.format(homemmaior+mulhermaior,mulhermaior,homemmaior))
print('Existe {} menores sendo {} mulheres e {} homens ' .format(mulhermenor+homemmenor,mulhermenor,homemmenor))
print('foram digitados {} dados invalidos '.format(invalidos))

    