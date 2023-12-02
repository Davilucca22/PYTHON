from datetime import datetime
ano_atual = datetime.today().year
ano = int(input('ano de nascimento do atleta:'))
idade = ano_atual - ano
if idade <= 9 :
    print('categoria:MIRIM')
elif idade > 9 and idade <= 14:
    print('categoria:INFANTIL')
elif idade > 14 and idade <= 19:
    print('categoria:JUNIOR')
elif idade == 20:
    print('categoria:SENIOR')
elif idade > 20:
    print('categoria:MASTER')
