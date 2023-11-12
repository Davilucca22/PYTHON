valor = float(input('QUAL O VALOR DO PRODUTO?:'))
desc = (valor*5)/100
novo_valor= valor - desc
print('O NOVO VALOR DO PRODUTO COM 5% DE DESCONTO É DE R${:.2f}'.format(novo_valor))
