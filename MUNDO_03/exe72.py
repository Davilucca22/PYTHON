numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

entrada = int(input('digite um numero entre 0 e 20:'))

while entrada > 20 or entrada < 0:
    entrada = int(input('tente novamente.digite um numero entre 0  e 20:'))

print(f'voce digitou o numero {numeros[entrada]}')
