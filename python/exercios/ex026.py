frase=str(input('digite uma frase ')).strip().lower()
print('a letra A aparece {} vezes'.format(frase.count('a')))
print('a letra A aparece primeiro na {} possição '.format(frase.find('a')+1))
print('a ultima letra aparece na {} possição '.format(frase.rfind('a')+1))
