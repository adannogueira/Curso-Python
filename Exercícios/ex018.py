# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite um ângulo para saber o seno, cosseno e tangente: '))
angrad = math.radians(ang)
seno = math.sin(angrad)
coss = math.cos(angrad)
tang = math.tan(angrad)
print(f'Para {ang}°, o seno é {seno:.2f}, o cosseno é {coss:.2f} e a tangente é {tang:.2f}')
