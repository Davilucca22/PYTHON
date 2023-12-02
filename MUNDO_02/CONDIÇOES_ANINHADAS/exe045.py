from random import randint
pc = randint(1,3)
jogador = int (input('vamos jogar!!\n[1]pedra\n[2]papel\n[3]tesoura\n:'))
if pc == 1:
    print('pc jogou pedra')
elif pc == 2:
    print('pc jogou papel')
elif pc == 3:
    print('pc jogou tesoura')
if pc == 1 and jogador == 1:
    print('empate')
elif pc == 1 and jogador == 2:
    print('voce venceu!')
elif pc == 1 and jogador == 3:
    print('voce perdeu!')
elif pc == 2 and jogador == 1:
    print('voce perdeu!')
elif pc == 2 and jogador == 2:
    print('empate')
elif pc == 2 and jogador == 3:
    print('voce venceu!')
elif pc == 3 and jogador == 1:
    print('voce venceu')
elif pc == 3 and jogador == 2:
    print('voce perdeu!')
elif pc == 3 and jogador == 3:
    print('empate')
