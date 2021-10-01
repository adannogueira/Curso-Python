# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que casa litro de tinta, pinta uma área de 2m².

print('Então você vai pintar a parede, me diga as medidas.')
alt = float(input('Altura em metros: '))
lar = float(input('Largura em metros: '))
ar = alt * lar

print(f'A área a ser pintada é de {lar} x {alt} = {ar:.2f}m²\nSerão necessários {ar/2:.3f}l de tinta.')
