lista=[[0,0,0],[0,0,0],[0,0,0]]
somapar=somaterceira=0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c]=int(input(f'Digite o valor da posição [{l},{c}] :'))
for l in range (0,3):
    for c in range(0,3):
        if lista[l][c]%2==0:
            somapar+=lista[l][c]
        if c ==2:
            somaterceira+=lista[l][c]
        print(f'[{lista[l][c]:^5}]',end=' ')
    print()
print(f'A soma dos numeros pares é :{somapar}')
print(f'A soma dos numeors da coluna 3 é :{somaterceira}')
print(f'O maior valor da segunda linha é :{max(lista[1])}')