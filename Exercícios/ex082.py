# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

nums = list()
while 1:
    nums.append(int(input("Digite um número inteiro: ")))
    cont = input('Digitar mais números?[S/N] ')
    if cont[0] in 'nN':
        break

npar = list()
nimp = list()

for num in nums:
    if num % 2 ==0:
        npar.append(num)
    else:
        nimp.append(num)

print(f'Lista original: {nums}')
print(f'Lista pares: {npar}')
print(f'Lista ímpar: {nimp}')