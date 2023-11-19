frase = input('digite uma frase:').upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a letra A aparece primeiro na posiça {}'.format(frase.find('A')+1))
print('a letra A aparece por ultimo na posiçao {}'.format(frase.rfind('A')+1))