""" Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint # função que gera números inteiros aleatórios
from time import sleep  # função para fazer esperar

computador = randint(0, 5) # Faz o computador sortear um número. 
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual é ...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(3)
# Condicionais
if jogador == computador:
    print('Parabens! Você ganhou!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}.'.format(computador, jogador))
print('Fim')


