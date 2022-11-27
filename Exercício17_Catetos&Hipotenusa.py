""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# A primeira forma de resolver o problema é este: 

co = float(input('Comprimento o cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))
"""

# Outra forma de resolver este exercício é utilizando funções. 

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hypot é a função para descobrir a hipotenusa. 
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))

