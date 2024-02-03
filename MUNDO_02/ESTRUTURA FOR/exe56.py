nome = [0 for x in range(4)] 
idade = [0 for x in range(4)]
sexo = [0 for x in range(4)]

print('-'*30)
for c in range(0,4):
    nome[c] = str(input(f'nome da {c+1}º pessoa:').lower())
    idade[c] = int(input(f'idade da {c+1}º pessoa:'))
    sexo[c] = str(input(f'sexo da {c+1}º pessoa:').lower()[0])
    print('-'*30)

soma = 0

for c in range(0,4):
    soma = soma + idade[c]

media = soma / 4

print('-'*30)
print(f'media de idade do grupo:{media}')

mais_velho = idade[0]

for c in range(0,4):
    if idade[c] >= mais_velho and sexo[c] == 'm':
        print(f'o homem mais velho é o {nome[c]}')

cont = 0

for c in range(0,4):
    if idade[c] < 20 and sexo[c] == 'f':
        cont = cont + 1

print(f'{cont} mulheres tem menos de 20 anos!')
