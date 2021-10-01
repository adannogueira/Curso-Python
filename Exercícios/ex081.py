# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

nums = list()
while 1:
    nums.append(int(input("Digite um número inteiro: ")))
    cont = input('Digitar mais números?[S/N] ')
    if cont[0] in 'nN':
        break
print(f'Você digitou {len(nums)} números.')
print(f'A ordem inversa é: ', end='')
nums.sort(reverse=True)
for num in nums:
    print(num, end=' > ')
print('Fim.')
if nums.count(5) > 0:
    print('O número 5 aparece na lista!')
else:
    print('O número 5 não está na lista.')
