from random import choice
a1=str(input('nome do primeiro aluno:'))
a2=str(input('nome do segundo aluno:'))
a3=str(input('nome do quarto aluno:'))
a4=str(input('nome do quarto aluno:'))
lista = [a1,a2,a3,a4]
alet = choice(lista)
print('o aluno escolhido foi {}'.format(alet))


