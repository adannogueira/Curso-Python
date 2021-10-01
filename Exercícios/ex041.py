# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
from datetime import date

idade = int(input("Digite o ano de nascimento do nadador: "))
categ = date.today().year - idade

if categ < 10:
    print("Categoria: Mirim")
elif categ < 15:
    print("Categoria: Infantil")
elif categ < 20:
    print("Categoria: Junior")
elif categ < 26:
    print("Categoria: Sênior")
else:
    print("Categoria: Master")
