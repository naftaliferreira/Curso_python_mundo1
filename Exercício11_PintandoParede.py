""" Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

larg = float(input('Digite a largura da parede: '))
altu = float(input('Digite a altura da parede: '))
# Calculando a área
area = larg * altu
print('Sua parede tem a dimênsão de {}x{} e sua área é de {}'.format(larg, altu, area))
# Calculando a quantidade de tinta
tinta = area / 2

print('Para pintar uma área de {} é necessário {} litros de tinta'.format(area, tinta))


