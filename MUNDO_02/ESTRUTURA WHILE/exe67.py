from time import sleep

numb = int  (input('digite um numero para ver sua tabuada:'))

while True:
    cont = 0
    print('-'*30)
    while cont <= 10:
        mult = numb * cont
        print(f'{numb} x {cont} = {mult}')
        cont += 1

    sleep(0.5)
    print('-'*30)
    numb = int  (input('digite um numero para ver sua tabuada:'))

    if numb < 0:
        break

print('-'*30)
print('programa tabuada encerrando...')
print('-'*30)
sleep(2)
print('fim')