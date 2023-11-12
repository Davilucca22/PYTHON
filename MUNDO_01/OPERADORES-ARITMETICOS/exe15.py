km = float(input('km percorridos pelo carro:'))
dias = int(input('dias de aluguel:'))
preço = km * 0.15 +  dias * 60
print('o valor total do veiculo é de R${:.2F}'.format(preço))