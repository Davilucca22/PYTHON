sexo = str(input('qual o seu sexo?[M/F]:').upper().strip()[0])


while sexo != 'M' and sexo != 'F':

    sexo = str(input('valor invalido,qual o seu sexo?[M/F]:').upper().strip()[0])

print(f'sexo {sexo} registrado com sucesso! ')