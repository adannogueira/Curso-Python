# Potenciação via fórmula

print(pow(4, 3))

# Raiz quadrada também utiliza potência, deixando o potenciador menor que 1

print(9**(1/2))

# Concatenação utilizando operadores

print('Oi'*5)

# Utilizações do .format

n = input('Digite seu nome: ')
print(f'Olá {n:=^20}, é um prazer!')

# Operadores

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
p = num1 ** num2

# "\n" quebra uma linha, "end=''" faz a linha continuar após o print()

print(f'A soma vale {s},\na multiplicação vale {m}, a divisão vale {d}', end=' ')
print(f'A divisão inteira vale {di}, a potenciação vale {p}.')
