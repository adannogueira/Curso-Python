# Faça um programa que leia o sexo de uma pessoa, mas só aceite os falores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = input('Digite o sexo (M/F): ')
while sex != 'M' and sex != 'F':
    sex = input('Digite o sexo (M/F): ')
print(f'Você digitou: {sex}')