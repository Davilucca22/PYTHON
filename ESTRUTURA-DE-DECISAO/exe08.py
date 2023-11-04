'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
pro_um=str(input('NOME DO PRIMEIRO PRODUTO:'))
valor_um=float(input('VALOR DO PRODUTO:'))
pro_dois=str(input('NOME DO SEGUNDO PRODUTO:'))
valor_dois=float(input('O VALOR DO PRODUTO:'))
pro_tres=str(input('NOME DO TERCEIRO PRODUTO:'))
valor_tres=float(input('DIGITE O VALOR DO PRODUTO:'))
barato=min(valor_um,valor_dois,valor_tres)
if barato == valor_um:
    print('VOCE DEVERÁ COMPRAR O PRODUTO {} QUE CUSTA R${}'.format(pro_um,valor_um))
elif barato == valor_dois:
    print('VOCE DEVERÁ COMPRAR O PRODUTO {} QUE CUSTA R${}'.format(pro_dois,valor_dois))
elif barato == valor_tres:
    print('VOCE DEVERÁ COMPRAR O PRODUTO {} QUE CUSTA R${}'.format(pro_tres,valor_tres))
