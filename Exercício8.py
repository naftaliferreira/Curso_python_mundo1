""" Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

# km              hm          dam         m        dm       cm        mm 
# 1000,0        100,0        10,0         1         0.1     0,01      0,001


medida = float(input('Digite a distância a ser convertida: '))

cm = medida * 100
mm = medida * 1000

print('A medida {} m em centímetros é {} cm'.format(medida, cm))
print('A medida {} m em milímetros é {} mm'.format(medida, mm))

