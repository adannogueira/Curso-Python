# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou o empréstimo será negado.

print("\033[34m=-\033[m" * 22)
print("Sistema de empréstimo residencial bancário.")
print("\033[34m-=\033[m" * 22)
casa = float(input("Informe o valor total do empréstimo: R$"))
salario = float(input("Informe o valor do salário: R$"))
prazo = int(input("Informe o prazo total em anos: "))

prestacao = casa / (prazo * 12)

if prestacao > (salario * 0.30):
    print("\033[31m=-" * 22)
    print("Infelizmente o valor da prestação excede\n30% do salário, o empréstimo não foi\nautorizado.")
    print(f"Valor da prestação R$ {prestacao:.2f}.")
    print("-=" * 22)
else:
    print("\033[32m=-" * 22)
    print(f"Seu financiamento foi aprovado!\nO valor das prestações será:\nR$ {prestacao:.2f}. Boa mudança.")
    print("-=" * 22)
