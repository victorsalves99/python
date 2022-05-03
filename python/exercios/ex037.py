print('-='*20)
numero=int(input('escolha um numero inteiro '))
print('-='*20)
print(''' Escolha uma das opções 
[1] BINARIO
[2] OCTAL
[3] HEXADECINAL  ''')
escolha=int(input('sua escolha '))
if escolha==1:
    print('o numeoro binario de {} é {}'.format(numero,bin(numero)[2:]))
elif escolha==2:
    print(' o numero octal de {} é {} '.format(numero,oct(numero)[2:]))
elif escolha==3:
    print('o numero hexadecimal de {} é {} '.format(numero,hex(numero)[2:]))
else:
    print('voce escolheu uma opção inezistente ')
