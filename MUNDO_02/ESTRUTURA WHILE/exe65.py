numb = int(input('digite um numero:'))
esc = str(input('continuar?[S/N]:').upper())

cont = 0
soma = 0
maior = numb
menor = numb

while esc != 'N':
    cont +=1
    soma += numb

    numb = int (input('digite um numero:'))
    esc = str(input('continuar?[S/N]:').upper())

    if numb > maior:
        maior = numb
    elif numb < menor:
        menor = numb

print('-'*35)
if cont >= 1:
    media = soma / cont
    print(f'media dos numeros lidos:{media:.2f}')
else:
    print('impossivel calcular a média!')

print(f'maior numero lido:{maior}')
print(f'menor numero lido:{menor}')
print('-'*35)
