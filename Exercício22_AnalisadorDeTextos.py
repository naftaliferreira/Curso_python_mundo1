"""  Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome. """

nome = str(input('Digite um nome: ')).strip()

print('Analisando o seu nome ...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # Com este comando é eliminado a contagem do espaço quando a pessoa tem dois nomes: Ana Julia, Ana Maria e etc. 

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Outra forma de fazer este último. 
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

