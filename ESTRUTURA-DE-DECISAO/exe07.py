'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
numum=int(input('DIGITE UM NUMERO:'))
numdois=int(input('DIGITE OUTRO NUMERO:'))
numtres=int(input('DIGITE MAIS UM NUMERO:'))
maior=max(numum,numdois,numtres)
menor=min(numum,numdois,numtres)
print('O MAIOR NUMERO É O NUMERO {} E O MENOR NUMERO É O NUMERO {}'.format(maior,menor))