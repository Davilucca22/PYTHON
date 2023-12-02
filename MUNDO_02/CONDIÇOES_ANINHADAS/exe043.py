peso = float(input('peso em kg:'))
altura = float(input('altura em m:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('status:ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('status:PESO IDEAL')
elif imc > 25 and imc <=30:
    print('status:SOBREPESO')
elif imc > 30 and imc <= 40:
    print('status:OBESIDADE')
elif imc > 40:
    print('status:OBESIDADE MORBIDA')
