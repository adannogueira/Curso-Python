# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / altura ** 2

if imc < 18.5:
    print("\033[31mAbaixo do peso.\033[m")
elif imc < 25:
    print("\033[32mPeso ideal.\033[m")
elif imc < 31:
    print("\033[33mSobrepeso.\033[m")
elif imc < 41:
    print("\033[31mObesidade.\033[m")
else:
    print("\033[2;31mObesidade mórbida.\033[m")
