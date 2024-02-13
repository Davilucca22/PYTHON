numb = int(input('digite um numero:'))

soma = 0
cont = 0

while numb != 999:
    cont += 1
    soma += numb
    numb = int (input('digite um numero:'))

print('-'*30)
print(f'foram digitados {cont} numeros,e')
print(f'a soma dos numeros lidos é {soma}')
print('-'*30)
 