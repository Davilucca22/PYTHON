'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas'''
pesopeixe = float(input('QUANTOS QUILOS DE PEIXE FORAM PESCADOS?:'))
excesso = pesopeixe - 50
multa = excesso * 4.00
if pesopeixe > 50:
    print('FORAM PESCADOS {}KG DE PEIXE A MAIS,COM ISSO JOAO DEVERA PAGAR UMA MULTA NO VALOR DE R${}'.format(excesso,multa))
else:
    print('NAO OUVE EXCESSO DE PEIXES PESCADOS!')