from random import randint
numeros = (randint(0,11),randint(0,11),randint(0,11),randint(0,11),randint(0,11))

print('os valores sorteados foram:',end='')
for c in range(0,len(numeros)):
    print(f'{numeros[c]}',end=' ')

print()
print(f'o maior valor é {max(numeros)}')

print(f'o menor valor é {min(numeros)}')

 
