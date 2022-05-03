tabela=('santos',	'Athletico-PR','Atlético-GO','Atlético-MG','Avaí',	'Botafogo','Bragantino',	'Ceará','Corinthians','Coritiba','Cuiabá','Flamengo','Fluminense','Fortaleza','Goiás','Internacional','Juventude','Palmeiras','América-MG','São Paulo')
print('-='*30)
print(f'TABELA DO BRASILEIRÃO {tabela}')
print('-='*30)
print(f'SINCO PRIMEIROS COLOCADOS {tabela[0:5]}')
print('-='*30)
print(f'SINCO ULTIMOS {tabela[-4:]}')
print('-='*30)
print(f'Os sinco em ordem alfabetica {sorted(tabela)}')
print('-='*30)
print(f'POSIÇÃO DO CORINTHIANS {tabela.index("Corinthians")+1}')
print('-='*30)


