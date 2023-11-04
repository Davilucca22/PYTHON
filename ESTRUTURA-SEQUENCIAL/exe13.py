'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
h=float(input('DIGITE SUA ALTURA EM CM:'))
homem=(72.7*h) - 58
mulher=(62.1*h) - 44.7
print('O PESO IDEAL PARA HOMENS É DE {:.2f}KG'.format(homem))
print('O PESO IDEAL PARA MULHERES É DE {:.2f}KG'.format(mulher))