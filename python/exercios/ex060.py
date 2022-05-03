import time
opcao=0
while opcao!=5:  
    n1=int(input('digite o primeiro valor :'))
    n2=int(input('digite o segundo valor :'))
    print('-='*15)
    print('''
    [1] SOMA 
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIGITAR NUMEROS NOVOS
    [5] SAIR DO PROGRAMA    ''')
    opcao=int(input('Escolha a opção :'))
    if opcao==1:
        print('a soma entre {} e {} é {} '.format(n1,n2,n1+n2))
    elif opcao==2:
        print('A multiplicação de {} e {} é {}  '.format(n1,n2,n1*n2))
    elif opcao==3:
        if n1>n2:
            print('O maior valor é {}'.format(n1))
        else:
            print('O maior valor é {} '.format(n2))
    elif opcao==4:
        print('digite novos numeros ')
    elif opcao>5 or opcao<1:
        print('Dados invalidos ')
print('Finalizando...')
time.sleep(2)
print('O programa foi finalizado !')
print('Obrigado volte sempre !')
    