from datetime import datetime
cidadao={}
cidadao['nome']=str(input('Nome: ')).strip().upper()
nac=int(input('ano de nascimento: '))
cidadao['idade']=datetime.now().year -nac
cidadao['carteira']=int(input('Carteira de trabalho (0 não tem ) : '))
if cidadao['carteira']!=0:
    cidadao['contratado']=int(input('Ano da Contratação : '))
    cidadao['salario']=float(input('Sálario : R$'))
    cidadao['aposentadoria']=cidadao['idade']+((cidadao['contratado']+35)-datetime.now().year)
print('-='*30)
for k,v in cidadao.items():
    if k == 'salario':
        print(f'- {k} tem valor R${v:.2f} ')
    else:
        print(f'- {k} tem valor {v} ')
