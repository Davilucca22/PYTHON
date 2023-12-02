reta_1 = float(input('comprimento da primeira reta:'))
reta_2 = float(input('comprimento da segunda reta:'))
reta_3 = float(input('comprimento da terceira:'))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    if reta_1 == reta_2 and reta_1 == reta_3 and reta_2 == reta_3:
        print('essas retas formam um triangulo equilatero')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('essas retas podem formar um triangulo isóceles')
    elif reta_1 != reta_2 and reta_1 != reta_3 and reta_2 != reta_3:
        print('essas retas podem formar um triangulo escaleno')
else:
    print('essas retas nao podem formar um triangulo')
 