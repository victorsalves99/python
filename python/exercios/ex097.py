def ariaTerreno(a,b):
    s=a*b
    print(f'A área de um terreno {a:.1f} x {b:.1f} é de {s:.1f}m²')


print(f'Controle de terrenos')
print('-'*30)
ariaTerreno(float(input('LARGURA(m): ')),float(input('CUMPRIMENTO(m): ')))
