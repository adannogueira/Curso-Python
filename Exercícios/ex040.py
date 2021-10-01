# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final.
# de acordo com a média atingida.
# Média abaixo de 5, reprovado
# Média entre 5 e 6.9, recuperação
# Média 7 ou superior, aprovado.

n1 = float(input("Digite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
med = (n1 + n2) / 2

if med < 5:
    print("Sua média está abaixo de 5, \033[2;31mREPROVADO.\033[m")
elif med >= 7:
    print(f"Sua média é {med:.1f}, \033[32m APROVADO.\033[m")
else:
    print("Sua média está abaixo de 7, \033[33mRECUPERAÇÃO.\033[m")