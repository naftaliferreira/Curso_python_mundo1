""" Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format(nome[:5] == 'Silva'))
# Ou 
print('Seu nome tem Silva? {}'.format('Silva' in nome.lower()))

