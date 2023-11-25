import datetime
ano = int (input('digite um ano(digite 0 para o ano atual):'))
atual = datetime.datetime.today().year
if ano == 0:
    if atual % 4 == 0 and atual % 100 != 0 or atual % 400 == 0:
        print(f'o ano {atual} é bissexto')
    else:
        print(f'o ano {atual} nao é bissexto')
if ano != 0:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'o ano {ano} é bissexto')
    else:
        print(f'o ano {ano} nao é bissexto')
