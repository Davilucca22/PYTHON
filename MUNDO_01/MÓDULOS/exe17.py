from math import hypot
oposto = float(input('medida do cateto oposto:'))
adjacente = float(input('medida do cateto adjacente:'))
print('a hipotenusa deste triangulo é de {:.2f}'.format(hypot(oposto,adjacente)))
