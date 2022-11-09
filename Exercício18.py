""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

import math 


an = float(input('Digite o ângulo que você deseja: '))
# pega o ângulo converte para radiano e depois calcula o seno.
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print('O ângulo {} tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente {:.2f}'.format(an, seno, cosseno, tangente))

# Para não ter que importar toda a biblioteca math, basta importar apenas as funções tan sen cos:   from math import sin, cos, tan

