from random import randint

alet = randint(0,10)

cont = 1

print('-'*30)
tent = int(input('pensei em um numero entre 0 e 10,tente adivinhar:'))

while tent != alet:
    if tent != alet:
        print('INCORRETO!')
        cont += 1

    tent = int(input('pensei em um numero entre 0 e 10,tente adivinhar:'))

print('-'*30)
print('correto!')
print(f'voce precisou de {cont} palpites para ganhar o jogo')
print('-'*30)