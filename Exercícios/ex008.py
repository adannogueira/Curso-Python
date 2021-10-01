# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
print("\033[32m+-\033[m" * 10)
print(f'Você informou {m}m.\nQue equivalem a:\n{m*10:.0f}dm\n{m*100:.0f}cm\n{m*1000:.0f}mm.')
print(f'{m/10}dam\n{m/100}hm\n{m/1000}km')