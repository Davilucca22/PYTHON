'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A.o produto do dobro do primeiro com metade do segundo .
B.a soma do triplo do primeiro com o terceiro.
C.o terceiro elevado ao cubo.'''
numum=int(input('DIGITE UM NUMERO INTEIRO:'))
numdois=int(input('DIGITE OUTRO NUMERO INTEIRO:'))
numreal=float(input('DIGITE UM NUMERO REAL:'))
A=(numum*2)+(numdois/2)
B=(numum*3) + numreal
C=pow(numreal,3)
print('O PRODUTO DO DOBRO DO PRIMEIRO COM METADE DO SEGUNDO É IGUAL A {:.0f}'.format(A))
print('A SOMA DO TRIPLO DO PRIMEIRO COM O TERCEIRO É IGUAL A {}'.format(B))
print('O TERCEIRO ELEVADO AO CUBO É IGUAL A {}'.format(C))
