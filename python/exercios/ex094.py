gol=[]
jogador={}
jogador['nome']=str(input('Nome : '))
partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou ? : '))
for c in range(0,partidas):
    gol.append(int(input(f'    Quantos gols na partida {c+1} :')))
jogador['gols']=gol[:]
jogador['totoal']=sum(gol)
print('-='*30)
print(f'{jogador}')
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos,c in enumerate(gol):
    print(f'    => Na partida {pos+1}, fez {c} gols. ')
print(f'Foi um total de {jogador["totoal"]} gols.')
