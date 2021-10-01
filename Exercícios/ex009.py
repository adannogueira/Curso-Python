# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('\033[31m===Tabuada===\033[m')
n = int(input('Digite um número: '))

print('\n# Multiplicação')
print(f'{n} x 1={n}\n{n:2} x 2={n*2}\n{n} x 3={n*3}\n{n} x 4={n*4}\n{n} x 5={n*5}')
print(f'{n} x 6={n*6}\n{n} x 7={n*7}\n{n} x 8={n*8}\n{n} x 9={n*9}\n{n} x10={n*10}')

print('\n# Divisão')
print(f'{n}/ 1={n}\n{n}/ 2={n/2:.2f}\n{n}/ 3={n/3:.2f}\n{n}/ 4={n/4:.2f}\n{n}/ 5={n/5:.2f}')
print(f'{n}/ 6={n/6:.2f}\n{n}/ 7={n/7:.2f}\n{n}/ 8={n/8:.2f}\n{n}/ 9={n/9:.2f}\n{n}/10={n/10:.2f}')

print('\n# Soma')
print(f'{n}+ 1={n+1}\n{n}+ 2={n+2}\n{n}+ 3={n+3}\n{n}+ 4={n+4}\n{n}+ 5={n+5}')
print(f'{n}+ 6={n+6}\n{n}+ 7={n+7}\n{n}+ 8={n+8}\n{n}+ 9={n+9}\n{n}+10={n+10}')

print('\n# Subtração')
print(f'{n}- 1={n-1}\n{n}- 2={n-2}\n{n}- 3={n-3}\n{n}- 4={n-4}\n{n}- 5={n-5}')
print(f'{n}- 6={n-6}\n{n}- 7={n-7}\n{n}- 8={n-8}\n{n}- 9={n-9}\n{n}-10={n-10}')
