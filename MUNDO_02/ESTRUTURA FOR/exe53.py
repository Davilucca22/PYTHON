entrada = str(input('digite uma palavra ou frase:').strip().upper())

mamao = entrada.split()

lista = ''.join(mamao)
invert = ''

for c in range(len(lista) -1 ,-1,-1):
    invert = invert + lista[c]

if invert == lista:
    print('temos um palindromo!')
else:
    print('nao temos um palindromo!')
