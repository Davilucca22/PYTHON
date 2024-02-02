'''corrigir'''

entrada = str(input('digite uma palavra ou frase:').strip())

mamao = entrada.split()

lista = ''.join(mamao)
invert = lista[::-1]

print(invert)
print(lista)

if lista == invert:
    print('-'*30)
    print('essa palavra é um palindromo!')
    print('-'*30)
else:
    print('-'*30)
    print('essa palavra nao é um palindromo!')
    print('-'*30)

