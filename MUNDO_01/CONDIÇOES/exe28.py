from random import randint
sorteio = randint(0,5)
while True:
    numero = int (input('tente adivinhar o numero q pensei:').strip())
    if numero == sorteio:
        print('\033[0;32mcerta resposta!!'+'\033[m')
        break
    else:
        print('\033[0;31merrado!'+'\033[m')
