valor_casa = float(input('qual o valor da casa?:').strip())
salario = float(input('qual o valor do seu salario?:').strip())
anos = int(input('em quantos anos vai pagar as parcelas da casa?:').strip())
prestacao_mensal = (valor_casa / anos) / 12
limite = (salario*30) / 100
if prestacao_mensal >= limite:
    print(f'o valor das parcelas mensais seriam de R${prestacao_mensal:.2f},esse valor excede 30% do seu salario.\nentao seu imprestimo foi \033[031mnegado!'+'\033[m')
elif prestacao_mensal <= limite:
    print(f'empretimo \033[0;32maceito\033[m!\nvoce deverá pagar R${prestacao_mensal:.2f} por mes,durante {anos} anos')
