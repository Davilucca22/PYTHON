'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
numero_um=int(input('DIGITE UM NUMERO:'))
numero_dois=int(input('DIGITE OUTRO NUMERO:'))
numero_tres=int(input('MAIS UM NUMERO:'))
maior=max(numero_um,numero_dois,numero_tres)
menor=min(numero_um,numero_dois,numero_tres)
if numero_um > numero_dois and numero_um < numero_tres:
    print('{},{},{}'.format(maior,numero_um,menor))
elif numero_um < numero_dois and numero_um > numero_tres:
    print('{},{},{}'.format(maior,numero_um,menor))
if numero_dois > numero_um and numero_dois < numero_tres:
    print('{},{},{}'.format(maior,numero_dois,menor))
elif numero_dois < numero_um and numero_dois > numero_tres:
    print('{},{},{}'.format(maior,numero_dois,menor))
if numero_tres > numero_um and numero_tres < numero_dois:
    print('{},{},{}'.format(maior,numero_tres,menor))
elif numero_tres < numero_um and numero_tres > numero_dois:
    print('{},{},{}'.format(maior,numero_tres,menor))