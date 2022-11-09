""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. """

from random import choice

# Nome dos alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# criação da lista alunos
alunos = [n1, n2, n3, n4]

# Escolher apenas 1 aluno
escolhido = choice(alunos)
# Exibir o resultado 
print('O aluno escolhido é {}'.format(escolhido))
