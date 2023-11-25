velocidade = float(input ('qual a velocidade do carro?:'))
if velocidade >= 80 :
    multa = (velocidade - 80) * 7.0
    print('\033[0;31mvoce foi multado!\033[m')
    print(f'o valor da multa é de R${multa}')
else:
    print('\033[0;32mvoce esta no limite de velocidade permitido!\033[m')
print('dirija com segurança!')