'''Faça um Programa que peça dois números e imprima o maior deles.'''
primeiro = int (input('DIGITE UM NUMERO:'))
segundo = int (input ('DIGITE OUTRO NUMERO:'))
if primeiro > segundo:
    print('O MAIOR NUMERO É {}'.format(primeiro))
else:
    print('O MAIOR NUMERO É {}'.format(segundo))