n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
n3 = int(input('digite um numero:'))
n4 = int(input('digite um numero:'))

numeros = (n1,n2,n3,n4)

print(numeros)

print(f'o numero 9 aparece {numeros.count(9)} vezes')

if numeros.count(3) > 0:
    print(f'o primeiro 3 foi digitado na posiçao {numeros.index(3)+1}')
else:
    print('nao foi digitado nenhum numero 3')

print('os numeros pares digitados sao:',end='')
for c in range(0,len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c],end=' ')