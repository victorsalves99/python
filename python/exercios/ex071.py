
total=0
acima=0
cont=0
nomemaior=''
nomemenor=''
while True:
    print('-='*30)
    print('LOJA DE PRODUTOS BARATOS ')
    print('-='*30)
    produto=str(input('Digite o nome do protudo :')).strip().upper()
    valor=int(input('Digite o valor do produto :R$'))
    total+=valor
    cont+=1
    if cont == 1:
        maior=valor
        menor=valor
        nomemaior = produto
        nomemenor=produto
    if valor>=1000:
        acima+=1
    if valor>maior:
        maior=valor
        nomemaior = produto
    if valor <menor:
        menor=valor
        nomemenor=produto
    res=''
    while res != 'SN':
        res=str(input('Quer continuar ? :')).strip().upper()[0]
    if res=='N':
        break
print(f'O total da sua compra foi {total} ')
print(f'Foram {acima} acima dos R$1000 ')
print(f'O maior valor do produto foi o { nomemaior} custando R${maior}')
print(f'O menor valor foi o {nomemenor} custando R${menor} ')
print('{:-^40}'.format( 'FIM DO PROGRAMA' ))

