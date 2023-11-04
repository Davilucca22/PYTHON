'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.'''
din=float(input('QUANTO VOCE GANHA POR HORA?:'))
hora=int(input('QUANTAS HORAS VOCE TRABALHA POR MES?:'))
sal=hora*din
renda=(sal*11) / 100
inss=(sal*8) / 100
sindicato=(sal*5) / 100
sobra=sal-renda-inss-sindicato
print('-'*30)
print('+ SALARIO BRUTO:R${:.2f}'.format(sal))
print('-IR(11%):R${:.2f}'.format(sal-renda))
print('-INSS(8%):R${:.2f}'.format(sal-inss))
print('-SINDICATO(5%):R${:.2f}'.format(sal-sindicato))
print('=SALARIO LIQUIDO:R${:.2f}'.format(sobra))
print('-'*30)
