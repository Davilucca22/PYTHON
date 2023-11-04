'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''
temp=int(input('DIGITE UMA TEMPERATURA EM GRAUS Fº:'))
c=5*((temp-32)/9)
print('ISSO REPRESENTA {:.1f}Cº'.format(c))