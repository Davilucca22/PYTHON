totcompra = maismil = barato = preco =  0
item = ''
while True:
    produto = str(input('produto:'))

    barato = preco

    preco = float(input('preço:R$'))

    if preco < barato:
        barato = preco
        item = produto

    totcompra = totcompra + preco

    if preco > 1000:
        maismil += 1 

    entrada = ' '
    while entrada not in 'SN':
        entrada = str(input('quer continuar?[S/N]:')).upper().strip()[0]

    if entrada == 'N':
        break

print('-'*35)
print(f'valor total da compra:R${totcompra:.2f}')
print(f'quantidade de produtos que custam mais de 1000 reais:{maismil}')
print(f'o produto mais barato é {item}')
print('-'*35)
