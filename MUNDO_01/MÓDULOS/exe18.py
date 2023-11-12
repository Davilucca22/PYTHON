from math import sin,cos,tan,radians
angulo =int (input('digite um angulo:'))
seno =sin(radians(angulo))
cosseno =cos(radians(angulo))
tang =tan(radians(angulo))
print('o seno de {} é {:.2f}'.format(angulo,seno))
print('o cosseno de {} é {:.2f}'.format(angulo,cosseno))
print('a tangente de {} é {:.2f}'.format(angulo,tang))
