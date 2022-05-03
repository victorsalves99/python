
produto=float(input('Qual o valor do produto ? '))
print('''Escolha a forma de pagamento 
[1] a vista no dinheiro : 10% de desconto 
[2] a vista no cartão : 5% de desconto 
[3] em 2x no cartão : preço normal 
[4] Em 3x no carrão : 20% de juros ''')
pagamento=int(input(''))
if pagamento==1:
    valordesconto=produto*10/100
    valorfinal=produto-valordesconto
    print('o valor do desconto é R${:.2f} e o valor total é de R${:.2f}'.format(valordesconto,valorfinal))
elif pagamento==2:
    valordesconto=produto*5/100
    valorfinal=produto-valordesconto
    print('O valor do desconto é de R${:.2f} e o valor final é de R${:.2f} '.format(valordesconto,valorfinal))
elif pagamento==3:
   
    parcelas=produto/2
    print('O valor do produto é R${:.2f} e fica 2x de R${:.2f}'.format(produto,parcelas))
elif pagamento==4:
    juros=produto*20/100
    valorfinal=produto+juros
    totalparcelas=int(input('Quantas parcelas ? '))
    parcelas=valorfinal/totalparcelas
    print('O valor do juros é de R${:.2f} valor total é de R${:.2f} fica {}x R${:.2f}'.format(juros,valorfinal,totalparcelas,parcelas))
else:
    print('Essa opção nao existe ! Porfavor escolher uma opção valida  ')

