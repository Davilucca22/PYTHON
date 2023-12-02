nota_1 = float(input('primeira nota:'))
nota_2 = float(input('segunda nota:'))
media = (nota_1 + nota_2) / 2
if media < 5 :
    print('\033[0;31maluno reprovado!\033[m')
elif media >= 5 and media <=6.9:
    print('\033[0;33maluno em recuperaçao!\033[m')
elif media >= 7:
    print('\033[0;32maluno aprovado!\033[m')
