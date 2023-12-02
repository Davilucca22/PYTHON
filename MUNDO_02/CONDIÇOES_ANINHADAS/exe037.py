num = int(input('digite um numero inteiro:'))
opc = int(input('numeros para base de conversao\n[1]binario\n[2]octal\n[3]hexadecimal\n:'))
if opc == 1:
    print(f'{num} convertido para binario é igual a {bin(num)[2:]}')
elif opc == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opc == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('valor invalido!')
