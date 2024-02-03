soma = 0
print('soma dos impares multiplos de tres entre 1 e 500:')

for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c

print(soma)