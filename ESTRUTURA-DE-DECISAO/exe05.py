'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
um=float(input('PRIMEIRA NOTA DO ALUNO:'))
dois=float(input('SEGUNDA NOTA DO ALUNO:'))
media=(um+dois)/2
if media >= 7.0 and media < 10:
    print('APROVADO!')
elif media == 10:
    print('APROVADO COM DISTINÇAO!')
else:
    print('REPROVADO!')

