maior = homem = mulher20=0
while True:
    print('-='*30)
    print('CADASTRO PESSOAL')
    print('-='*30)
    idade=int(input('Digite idade :'))
    sexo = str(input('Digite o sexo [M/F]:')).strip().upper()[0]
    if idade>=18:
        maior=maior+1
    if sexo == 'M':
        homem+=1
    if sexo=='F' and idade<=20:
        mulher20+=1
    continuacao=str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if continuacao=='N':
        break
print(f'Foram {maior} maiores de idade ')
print(f'Foram {homem} homens cadastrados ')
print(f'Fora {mulher20} mulheres com menos de 20 anos ')
    


