preço = float(input('valor a ser pago:'))
pagamento = int(input('forma de pagamento\n[1]dinheiro/cheque\n[2]a vista no cartao\n[3]2x no cartao\n[4]3x ou mais no cartao\n'))
dinheiro =  preço - ((preço*10) / 100)
a_vista = preço - ((preço*5) /100)
parcela_cartao = preço + ((preço*20) / 100)
if pagamento == 1:
    print(f'pagamentos com dinheiro ou cheque recebem 10% de desconto\nvalor a ser pago R${dinheiro:.2f}')
elif pagamento == 2:
    print(f'pagamentos a vista no cartao recebem 5% de desconto\nvalor a ser pago R${a_vista}')
elif pagamento == 3:
    print(f'pagamentos em 2x no cartao nao recebem desconto nem juros\nvalor a ser pago R${preço}')
elif pagamento == 4:
    print(f'parcelando 3x ou mais no cartao,é aplicado um juros de 20%\nvalor a ser pago R${parcela_cartao}')
