numb = soma = cont = 0

while True: 
    numb = int(input('digite um numero(999 para parar):'))

    if numb == 999:
     break

    cont += 1
    soma += numb
print('-'*30)
print(f'a soma dos {cont} numeros lidos é {soma}')
print('-'*30)