palavras = ('OSSO','SUPINO','FRONTEND','TRABALHO','COMPUTADOR','LEGPRESS','DORMIR','ESTUDAR','LER','JUNTAR')

for c in range(0,len(palavras)):
    print(f'na palavra {palavras[c]} temos',end=' ')
    if 'A' in palavras[c]:
        print('a')
    print()