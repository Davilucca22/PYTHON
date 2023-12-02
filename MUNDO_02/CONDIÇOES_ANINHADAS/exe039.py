from datetime import datetime
ano_atual = datetime.today().year
nascimento = int(input('em que voce nasceu?:'))
idade = ano_atual - nascimento
if idade < 18:
    print(f'voce devera se alistar em {18-idade} anos!')
elif idade == 18:
    print('voce deve se alistar este ano!')
elif idade > 18:
    print(f'voce deveria ter se alistado há {idade-18} anos!')
