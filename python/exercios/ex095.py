pessoas=[]
mulheres=[]
cadastro={}
acima=[]
resp=''
somaidade=0
while True:
    cadastro['nome']=str(input('Nome:')).strip() .upper()
    while True:
        cadastro['sexo']=str(input('Sexo:[M/F]'))[0]
        if cadastro['sexo'] in 'mMFf':
            if cadastro['sexo'] in 'fF':
                mulheres.append(cadastro['nome'])
            break
        print(f'ERRO! Por favor, digite apena M ou F')
    cadastro['idade']=int(input('idade:'))
    somaidade+=cadastro['idade']
    pessoas.append(cadastro.copy())
    while True:
        resp=str(input('Quer contunuar ?[S/N]'))
        if resp in 'sSnN':
            break
        print(f'ERRO! Por favor, digite apena S ou N')
    if resp in 'nN':
        break
media=somaidade/len(pessoas)
for cont in pessoas:
    for k,v in cont.items():
        if k =='idade' and v>media:
            acima.append(cont.copy())
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ',end='')
for c in (mulheres):
    print(f'{c}',end=', ')
print()
print(f'D) Lista das pessoas que estão acima da média :')
for c in acima:
    for k,v in c.items():
        print(f'    {k} = {v} ',end=';')
    print()
print('<<ENCERRADO>>')








        


