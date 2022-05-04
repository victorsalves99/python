nomes=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for item in nomes:
    print(f'\nO NOME {item} TEM ESSAS VOGAIS :',end='')
    for letra in item:
        if letra in'AEIOU':
            print(f"{letra}",end=' ')
    