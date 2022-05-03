import random
n1=input('digite o primeiro nome ')
n2=input('digite o segundo nome ')
n3=input('digite o terceiro nome ')
n4=input('digite o quator nome ')
lista=[n1,n2,n3,n4]
random.shuffle(lista)#escolhe a ordem  a ordem que a lista vai ser exibida
print('a ordem de apresentação sera ')
print(lista)
