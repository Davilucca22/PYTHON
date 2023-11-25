salario = float(input('qual o seu salario:'))
if salario >= 1250:
    novo_salario = ((salario*10)/100) + salario
    print(f'seu novo salario com 10% de aumento é de R${novo_salario}')
if salario <= 1250:
    novo_salario = ((salario*15) / 100) + salario
    print(f'seu novo salario com 15% de aumento é de R${novo_salario}')
