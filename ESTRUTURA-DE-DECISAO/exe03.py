'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
sex=str(input('QUAL O SEU SEXO?\n[F]PARA FEMININO\n[M]PARA MASCULINO\nRESPOSTA:'))
if sex == 'M':
    print('VOCE ESCOLHEU:MASCULINO')
elif sex == 'F':
    print('VOCE ESCOLHEU:FEMININO')
else:
    print('SEXO INVALIDO')