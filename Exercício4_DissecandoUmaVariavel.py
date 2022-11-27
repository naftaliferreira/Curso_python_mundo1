""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""

from curses.ascii import isalpha


var = input('Digite algo: ')

print(var.isalpha())
print(var.isalnum())
print(var.isdecimal())
print(var.isdigit())
print(var.isnumeric())
print(var.isupper())
print(var.islower())

