salario=float(input('qual o seu salario? '))
if salario>=1250:
    porcentagem=10
    almento=salario*porcentagem/100
else:
    porcentagem=15
    almento=salario*porcentagem/100
print('Voce ganhouu um almento de {}% , e seu novo salario é R$ {:.2f}'.format(porcentagem,almento+salario))
