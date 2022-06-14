nomes=list()
peso=list()
maispeso=list()
menospeso=list()
while True :
    nomes.append(str(input('Nome:')))
    peso.append(int(input('Peso:')))
    resp=str(input('Quer continuar : [S/N]: '))
    if resp in 'nN':
        break
print(f'Foram cadastradas {len(nomes)} pessoas')
maior=max(peso)
menor=min(peso)
for pos,c in enumerate(peso):
    if c==maior:
        maispeso.append(nomes[pos])
    if c==menor:
        menospeso.append(nomes[pos])
print(f'A pessoa mais pesada pesa {maior} KG é {maispeso}')
print(f'A pessoa mais leve pesa {menor} KG é {menospeso}')
