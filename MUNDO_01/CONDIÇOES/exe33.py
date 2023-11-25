numero_1 = int(input('digite um numero:'))
numero_2 = int(input('digite outro numero:'))
numero_3 = int(input('digite mais um numero:'))
if numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f'MAIOR NUMERO:{numero_1}')
if numero_2 >= numero_1 and numero_2 >= numero_3:
    print(f'MAIOR NUMERO:{numero_2}')
if numero_3 >= numero_1 and numero_3 >= numero_2:
    print(f'MAIOR NUMERO:{numero_3}')
if numero_1 <= numero_2 and numero_1 <= numero_3:
    print(f'MENOR NUMERO:{numero_1}')
if numero_2 <= numero_1 and numero_2 <= numero_3:
    print(f'MENOR NUMERO:{numero_2}')
if numero_3 <= numero_1 and numero_3 <= numero_2:
    print(f'MENOR NUMERO:{numero_3}')
