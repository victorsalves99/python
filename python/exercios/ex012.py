preco=float(input('qual o valor do produto ? '))
desconto=float(input('qual o valor do desconto ? '))
parcelas=int(input('quantas vezes quer dividir ? '))

valordescontado=preco*desconto/100
valorfinal= preco - valordescontado
valordasparcelas=valorfinal/parcelas

print('valor do produdo            R$ {:.2f}'.format(preco))
print('valor do desconto           R$ {:.2f}'.format(valordescontado))
print('valor final do produto      R$ {:.2f}'.format(valorfinal))
print('ficara {} parcelas de R${:.2f} '.format(parcelas,valordasparcelas))


