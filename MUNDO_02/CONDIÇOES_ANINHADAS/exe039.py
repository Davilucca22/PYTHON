from datetime import date

ano_atual = date.today().year
nascimento = int(input('em que voce nasceu?:'))
idade = ano_atual - nascimento
if idade < 18:
    print(f'voce devera se alistar em {18-idade+ano_atual}!')
elif idade == 18:
    print(f'voce deve se alistar este ano {ano_atual}!')
elif idade > 18:
    print(f'voce deveria ter se alistado em {ano_atual-(idade-18)}!')
