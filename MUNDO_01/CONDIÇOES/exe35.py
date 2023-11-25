reta_1 = float(input('comprimento da primeira reta:'))
reta_2 = float(input('comprimento da segunda reta:'))
reta_3 = float(input('comprimento da terceira:'))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('essas retas podem formar um triangulo')
else:
    print('essas retas nao podem formar um triangulo')
 