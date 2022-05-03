sexo = str(input('informe seu sexo :')).strip().upper()[0]
while sexo not in 'MF':
    sexo =str(input('Dados invalidos digite novamente ')).strip().upper()[0]
print('O sexo ({}) foi  cadastrado com sucesso '.format(sexo))
