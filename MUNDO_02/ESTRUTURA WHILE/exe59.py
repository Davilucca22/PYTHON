from time import sleep

n1 = int (input ('primeiro valor:'))
n2 = int (input ('segundo valor:'))

print('-'*30)
print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
print('-'*30)
menu = int(input('entrada:'))

while menu != 5:
    if menu == 1:
        print(f'a soma de {n1} + {n2} é igual a {n1+n2}')
    elif menu == 2:
        print(f'a multiplicaçao de {n1} * {n2} é igual a {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'o maior numero é o {n1}')
        else:
            print(f'o maior numero é o {n2}')
    elif menu == 4:
        n1 = int(input('primeiro valor:'))
        n2 = int(input('segundo valor:'))
    sleep(1)
    print('-'*30)
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    print('-'*30)
    menu = int(input('entrada:'))

print('fim')