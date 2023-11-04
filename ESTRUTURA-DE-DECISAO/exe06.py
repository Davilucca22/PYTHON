'''Faça um Programa que leia três números e mostre o maior deles.'''
numeroum=int(input('DIGITE UM NUMERO:'))
numerodois=int(input('DIGITE OUTRO NUMERO:'))
numerotres=int(input('DIGITE MAIS UM NUMERO:'))
if numeroum > numerodois and numeroum > numerotres:
    print('O MAIOR NUMERO É O NUMERO {}'.format(numeroum))
elif numerodois > numeroum and numerodois > numerotres:
    print('O MAIOR NUMERO É O NUMERO {}'.format(numerodois))
elif numerotres > numeroum and numerotres > numerodois:
    print('O MAIOR NUMERO É O NUMERO {}'.format(numerotres))