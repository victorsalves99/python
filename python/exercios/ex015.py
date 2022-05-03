diasusados=float(input('quantos dias ficou com o carro ? '))
kmusados=float(input('quantos quilometros percorridos ? '))
precodia=diasusados*60
precokm=kmusados*0.15
print('por {} dias voce pagara R${:.2f}'.format(diasusados,precodia))
print('pro {} KM voce pagara R$ {:.2f}'.format(kmusados,precokm))
print('total a pagar R${:.2f}'.format(precodia+precokm))
