""" Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. """

numero = int(input('Me diga um número qualquer: '))
# O resto da divisão de qualquer número par por 2 é zero, e o resto da divisão de um número impar por 2 é 1. 
resultado = numero % 2
if resultado == 0:
    print('O número {} é Par'.format(numero))
else: 
    print('O número {} é impar'.format(numero))

    
