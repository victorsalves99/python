gol=[]
jogador={}
jogadores=[]
while True:
    jogador['nome']=str(input('Nome : ')).upper()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou ? : '))
    for c in range(0,partidas):
        gol.append(int(input(f'    Quantos gols na partida {c+1} :')))
    jogador['gols']=gol[:]
    jogador['total']=sum(gol)
    jogadores.append(jogador.copy())
    gol.clear()
    jogador.clear()
    resp=str(input('Quer continuar ? : [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{"cod":<5} {"nome":<10} {"gols":<20} {"total":>5}')
print(f'-'*50)
for pos,j in enumerate(jogadores):
    print(f'{pos+1:<5} {j["nome"]:<10} {str(j["gols"]):<20} {j["total"]:>5}')
while True :
    dados=int(input('Mostrar dados de qual jogador?(999 para parar: '))-1
    if dados == 998:
        break
    elif dados>=0 and dados<len(jogadores):
        print(f'LEVANTAMENTO DO JOGADOR : {jogadores[dados]["nome"]}')
        dadosgols=jogadores[dados]['gols'][:]
        for pos,c in enumerate(dadosgols):
            print(f'No jogo {pos+1} fez {c} gols.')
    else:
        print(f'ERRO! escolha um numero de jogador que esteja na tabela')
print(f'    <<<Obrigado volte sempre!>>>   ')