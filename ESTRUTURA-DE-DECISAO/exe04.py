'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
letra=str(input('DIGITE QUALQUER LETRA:'))
if letra == 'A' or letra == 'E' or letra == 'I' or letra =='O' or letra == 'U':
    print('{} É VOGAL'.format(letra))
elif letra != 'A' or letra != 'E' or letra != 'I'or letra != 'O' or letra != 'U':
    print('{} É CONSOANTE'.format(letra))
