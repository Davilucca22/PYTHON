times = ('flamengo','palmeiras','sao paulo','athletico-pr','atletico-mg','corinthians','fluminense','gremio','fortaleza','america-mg','internacional','santos','bahia','botafogo','red bull bregantino','atletico-go','cruzeiro','ceara','cuiaba','goias')

print(50*'-')
print(f'TABELA DOS TIMES NO BRASILEIRAO:{times}')
print(50*'-')

print(f'OS CINCO PRIMEIROS COLOCADOS SAO:{times[:5]}')
print(50*'-')

print(f'OS ULTIMOS 4 COLOCAOS SAO:{times[-4:]}')
print(50*'-')

print(f'LISTA DOS TIMES EM ORDEM ALFABETICA:{sorted(times)}')
print(50*'-')

for c in range(0,len(times)):
    if times[c] == 'gremio':
        print(f'O GREMIO ESTA NA {c+1}º POSIÇAO DA TABELA')

print(50*'-')