listagem = ('teclado',50.25,'monitor',200.00,'mouse',25.50,'fone',10.50,'controle',45.99)

print('-'*30)
print('tabela de preços')
print('-'*30)

for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(listagem[c],end='_'*10)

    if c % 2 == 1:
        print(listagem[c])
