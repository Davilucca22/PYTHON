numb = int(input('digite um numero:'))

cont = 0
soma = 1

while cont <= numb:
    fibo = soma + cont
    print(fibo)
    cont += 1
    fibo += cont