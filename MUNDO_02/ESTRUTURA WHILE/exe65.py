numb = int(input('digite um numero:'))
esc = str(input('continuar?[S/N]:').upper())

cont = 1
soma = 0
maior = numb
menor = numb
soma += numb

while esc != 'N':
    cont += 1

    numb = int (input('digite um numero:'))
    esc = str(input('continuar?[S/N]:').upper())
    soma += numb

    if numb > maior:
        maior = numb
    elif numb < menor:
        menor = numb

print('-'*35)
if cont != 0:
    media = soma / cont
    print(f'media dos numeros lidos:{media:.2f}')
else:
    print('impossivel calcular a média!')

print(f'maior numero lido:{maior}')
print(f'menor numero lido:{menor}')
print('-'*35)
