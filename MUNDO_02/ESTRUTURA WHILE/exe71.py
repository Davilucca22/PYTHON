dinheiro = int(input('digite quanto quer sacar:R$'))

div1 = dinheiro % 50
div2 = dinheiro // 50
div3 = div1 % 20
div4 = div1 // 20
div5 = div3 // 10
div6 = div3 % 10

print(f'{div2} cedulas de R$50,00')
print(f'{div4} cedulas de R$20,00')
print(f'{div5} cedulas de R$10,00')
print(f'{div6} cedulas de R$1,00')