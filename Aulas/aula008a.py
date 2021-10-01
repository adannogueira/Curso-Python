import math  # Este método importa toda a bilioteca "math" e a deixa a disposição
# from math import sqrt  # Este método importa apenas a função a ser utilizada, dessa forma não é necessário usar a
# sintaxe "math.sqrt()", apenas sqrt()
num = int(input('Digite um número para ver a raiz quadrada: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}')

import random
ran = random.randint(1, 10)
print(ran)
