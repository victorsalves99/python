while True:   
    while True:
        n=int(input('Digite um numero :'))
        if n>=0 and n<=10:
            break

    lista=('zero', 'um', 'dois','tres','quatro','sinco','seis','sete','oito','nove','dez')
    print(f'O numero que voce digitou foi {lista[n]}')
    res=str(input('Quer continuar ? ')).strip().upper()[0]
    if res=='N':
        break