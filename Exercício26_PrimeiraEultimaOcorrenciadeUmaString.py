""" Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. """

frase = str(input('Digite uma frase: ')).upper().strip()
# string convertido para letra maiuscula e strip é para eliminar espaços indesejados. 
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A Última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # rfind = procura apartir do lado direito. 
