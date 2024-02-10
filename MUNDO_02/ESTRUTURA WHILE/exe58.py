from random import randint

alet = randint(0,10)

cont = 0

print('-'*30)
tent = int(input('pensei em um numero entre 0 e 10,tente adivinhar:'))
 
if tent != alet:
    print('INCORRETO!')
    cont += 1
else:
    print('CORRETO!!')

while tent != alet:
    print('-'*30)
    tent = int(input('tente novamente:'))

    if tent != alet:
        print('INCORRETO!')
        cont += 1
    else:
        print('CORRETO!!')

print('-'*30)
print(f'voce precisou de {cont} palpites para ganhar o jogo')
print('-'*30)