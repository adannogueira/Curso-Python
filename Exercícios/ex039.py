# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
hoje = date.today().year
idade = int(input("Olá, digite seu ano de nascimento: "))
mil = hoje - idade
if mil < 18:
    print(f"\033[32mVocê ainda pode esperar {18 - mil} ano(s) até se alistar.\033[m")
elif mil == 18:
    print("\033[33mEstá na hora de se alistar!\033[m")
else:
    print(f"\033[31mVocê está atrasado para o alistamento, já passou {mil - 18} ano(s) da hora!\033[m")
