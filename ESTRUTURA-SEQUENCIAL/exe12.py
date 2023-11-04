'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''
altura=float(input('DIGITE SUA ALTURA EM CM:'))
pesoideal=(72.7*altura) - 58
print('O PESO IDEAL PARA SUA ALTURA É DE {:.2f} KG'.format(pesoideal))