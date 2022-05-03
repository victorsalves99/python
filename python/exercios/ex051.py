print('-='*20)
print('PA  10 numeors ')
print('-='*20)
termo=int(input('digite o primeiro termo '))
rasao=int(input('digite a rasao '))
descimo=termo+(10-1)*rasao
for c in range(termo,descimo,rasao):
    print('{}'.format(c),end ='->')
print('acabou ')

