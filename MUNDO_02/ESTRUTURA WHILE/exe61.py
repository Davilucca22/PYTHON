ptermo = int(input('digite o primeiro termo:'))
razao = int(input('digite a razao:'))

soma = 0
cont = 1

print('-'*30)
print('primeiros 10 termos da PA')
print('-'*30)

while cont != 11:
    soma = ptermo + (cont - 1) * razao
    print(soma,end=' -> ')
    cont += 1

print('fim')
