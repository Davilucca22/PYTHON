dmaior = 0
homem = 0
mulher = 0

print('-'*35)
print('CADASTRO DE PESSOAS')
print('-'*35)

while True:
    idade = int(input('digite a idade da pessoa:'))
    if idade > 18:
        dmaior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo da pessoa[M/F]:')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    
    if sexo == 'F' and idade < 20:
        mulher += 1 

    entrada = ' '
    while entrada not in 'SN':
        print('-'*35)
        entrada = str(input('quer continuar?[S/N]:')).upper().strip()[0]
    if entrada == 'N':
        break
    print('-'*35)

print('-'*35)
print(f'quantidade de pessoas com mais de 18 anos:{dmaior}')
print(f'ao todo foram cadastrados {homem} homens')
print(f'ao todo {mulher} mulher(es) tem menos de 20 anos de idade')
