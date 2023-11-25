km = int (input('qual a distâcia da viagem em KM?:'))
if km <= 200:
    passagem = 0.50 * km
    print(f'para uma viagem de {km} KM o valor da passagem será de R${passagem}')
if km >= 200:
    passagem = 0.45 * km 
    print(f'para uma viagem de {km} KM o valor da passagem será de R${passagem}')
