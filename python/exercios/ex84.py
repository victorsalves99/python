abrir=fechar=falha=0

esprex=str(input('Digite sua expressão '))
for c in esprex:
    if c=="(":
        abrir+=1
    elif c==')':
        fechar+=1
    if fechar>abrir:
        falha+=1
if abrir==fechar:
    if falha!=0:
        print(f'A expressão está errada !')
    else:
        print(f'A expressão está certá !')
else:
    print(f'A expressão está errada !')
