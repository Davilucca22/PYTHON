'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
while True:
    periodo=str(input('QUAL PERIODO VOCE ESTUDA?\n[M]MATUTINO\n[V]VESPERINO\n[N]NOTURNO\nR:'))
    if periodo == 'M':
        print('BOM DIA!')
        break
    elif periodo == 'V':
        print('BOA TARDE!')
        break
    elif periodo == 'N':
        print('BOA NOITE!')
        break
    else:
        print('VALOR INVALIDO!')