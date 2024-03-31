from random import randint
cont = 0
pc = randint(0,10)

print('-'*35)
print('JOGO PAR OU IMPAR')
print('-'*35)
while True:
    
    ganhou = False
    perdeu = False

    jogador = int(input('digite um numero:'))

    jogada = str(input('par ou impar?[P/I]:').upper())

    result = jogador + pc
    print('-'*35)
    print(f'voce jogou {jogador} e pc jogou {pc}.total {result}')

    if result % 2 == 0 and jogada == 'P':
        ganhou = True

    elif result % 2 == 1 and jogada == 'I':
        ganhou = True

    elif result % 2 == 0 and jogada == 'I':
        perdeu = True

    elif result % 2 == 1 and jogada == 'P':
        perdeu = True

    if ganhou == True:
        cont += 1
        print('VOCE GANHOU!!')
        print('vamos jogar novamente')
        print('-'*35)
    else:
        print('VOCE PERDEU!')
        print('-'*35)
        print(f'voce venceu {cont} vezes')
        break
print('fim')
