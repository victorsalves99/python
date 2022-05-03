from ntpath import join


frase= str(input('digite uma frase ')).strip().upper()
fraseseparada=frase.split()
junto="".join(fraseseparada)
inverso=junto[::-1] #seguinifica que ele vai pegar a variave junto e do incio ate o fim so que de tras pra frente 
'''for letra in range(len(junto)-1,-1,-1):
    inverso=inverso+junto[letra]'''

    
if inverso==junto:
    print('a frase {} é um palindromo '.format(inverso))
else: 
    print('a frase {} nao é um palimdromo '.format(inverso))

