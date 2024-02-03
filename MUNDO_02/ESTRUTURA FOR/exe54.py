from datetime import date
ano_atual = date.today().year

dmenor = 0
dmaior = 0

for c in range(0,7):
    ano_nasc = int(input(f'digite o ano de nascimento da {c+1} pessoa:'))
    if ano_atual - ano_nasc < 21:
        dmenor = dmenor + 1
    else:
        dmaior = dmaior + 1
        
print('-'*30)
print(f'{dmenor} pessoas sao menores de idade!')
print(f'{dmaior} pessoas sao maiores de idade!')
print('-'*30)
