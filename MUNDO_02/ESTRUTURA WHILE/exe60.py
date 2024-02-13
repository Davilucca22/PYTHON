dig = int(input('digite um numero:'))

cont = 1
fat = 1

while dig >= cont :

    fat = fat * cont
    cont += 1

print('-'*30)
print(f'o fatorial de {dig} é {fat}')
print('-'*30)
