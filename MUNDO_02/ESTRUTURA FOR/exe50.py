soma = 0

for c in range(0,6):
    n = int(input(f'digite o {c+1}º numero:'))

    if n % 2 == 0:
        soma = soma + n
        
print('-'*30)
print(f'soma dos numeros pares:{soma}')
print('-'*30)
