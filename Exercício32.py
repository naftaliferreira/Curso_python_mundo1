''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

ano = int(input('Que ano quer analisar? '))
# Anos bissextos são divisíveis por 4, porem não podem ser divisíveis por 100 e ser divisível por 400.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO.'.format(ano))

else:
        print('O ano {} não é bissexto'.format(ano))

# Em caso de alguma condicional não está funcionando, basta verificar as indentações.

