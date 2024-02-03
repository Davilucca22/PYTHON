vet = [0 for x in range (5)]

for c in range(0,5):
    vet[c] = float(input(f'digite o peso da {c+1}º pessoa:'))

maior = vet[0]

for c in range(0,5):
    if vet[c] > maior:
        maior = vet[c]

menor = vet[0]

for c in range(0,5):
    if vet[c] < menor:
        menor = vet[c]

print('-'*30)
print(f'maior peso:{maior} kg')
print(f'menor peso:{menor} kg')
print('-'*30)