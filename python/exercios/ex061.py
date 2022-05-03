import math
n=int(input('Qual numero quer seber  o fatorial? :'))
f=math.factorial(n)
c=n
while c>0 :
    print('{} '.format(c), end='')
    print('x' if c>1 else '=',end=' ')

    c-=1
print(f,end='')
