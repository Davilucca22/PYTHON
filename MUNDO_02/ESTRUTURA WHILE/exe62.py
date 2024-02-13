ptermo = int (input('digite o primeiro termo:'))
razao = int (input('digite a razao:'))

termos = int(input('deseja ver quantos termos?:'))

soma = 0
cont = 1
contermo = 0

while termos != 0:
    cont = 1
    contermo += termos

    while cont != contermo+1:

        soma = ptermo + (cont - 1) * razao
        print(soma,end=' -> ')
        cont += 1
    print('fim')

    termos = int(input('deseja ver quantos termos?:'))

print('fim')
