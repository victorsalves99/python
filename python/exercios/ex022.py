nome= str(input('qual o seu nome ? ')).strip()
print('seu nome é {}'.format(nome))
print('maiusculo é {}'.format(nome.upper()))
print('minuscula é {}'.format(nome.lower))
print('nome {} tem {} letras'.format(nome,len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} '.format(separa[0]))
print('seu primeiro nome tem {} letras'.format(len(separa[0])))





