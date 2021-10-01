# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.

a = float(input("Digite o tamanho do lado a: "))
b = float(input("Digite o tamanho do lado b: "))
c = float(input("Digite o tamanho do lado c: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Estes três lados formam um triângulo.")
else:
    print("É impossível formar um triângulo com essas medidas.")
