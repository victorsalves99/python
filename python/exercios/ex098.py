def escreva(t):
    print('~'*(len(t)+4))
    print(f'  {t}')
    print('~'*(len(t)+4))

while True:
    escreva(str(input('Digite uma frase: ')))
    resp=str(input('Quer continuar ? : '))
    if resp in 'Nn':
        break
    