'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
din=float(input('QUANTO VOCE GANHA POR HORA?:'))
hora=int(input('QUANTAS HORAS VOCE TRABALHA POR MES?:'))
sal=hora*din
print('VOCE GANHA UM TOTAL DE R${} REAIS POR MES.'.format(sal))
