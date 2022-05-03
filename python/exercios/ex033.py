n1=int(input('digite o priemiro numero '))
n2=int(input('digite o segundo numero '))
n3=int(input('digite o terceiro numero '))
#if n1>n2 and n3:
    #maiorvalor=n1
#if n2>n1 and n3:
   # maiorvalor=n2
#if n3>n1 and n2:
  #  maiorvalor=n3
#if n1<n2 and n3:
  #  menorvalor=n1
#if n2<n1 and n3:
   # menorvalor=n2
#if n3<n1 and n2 :
   # menorvalor=n3
maiorvalor=n1
if n2>n1 and n3:
    maiorvalor=n2
if n3>n1 and n3> n2:
    maiorvalor=n3

menorvalor=n1
if n2<n1 and n3:
    menorvalor=n2
if n3<n1 and n2 :
    menorvalor=n3
print('o maior valor digitado foi {} '.format(maiorvalor))
print('o menor valor digitado foi {} '.format(menorvalor))
