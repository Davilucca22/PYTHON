ptermo = int(input('digite o primeiro termo da PA:'))
razao = int(input('digite a razao:'))

soma = 0

print('-'*30)
print('primeiros 10 termos:')
print('-'*30)

for c in range(1,11):

    soma = ptermo + (c - 1) * razao
    print(soma)

print('-'*30)


    
    
    