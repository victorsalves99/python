aluno={}
aluno['nome']=str(input('Nome:'))
aluno['media']=float(input(f'média de {aluno["nome"]}:'))
if aluno['media']<= 5:
    aluno['situação']="reprovado"
elif 5<= aluno['media']<=7:
    aluno['situação']="recuperação"
else:
    aluno['situação']="aprovado"
print('-'*30)
for k,v in aluno.items():
    print(f'{k} = {v}')

    