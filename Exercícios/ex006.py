# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print(f'Você digitou o número \033[35m{n}\033[m.\nO dobro é \033[35m{n * 2}\033[m.')
print(f'O triplo é \033[35m{n * 3}\033[m.\nA raiz quadrada é \033[35m{n ** (1/2):.2f}\033[m.')
