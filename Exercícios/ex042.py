# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: Todos os lados diferentes
a = float(input("Digite o tamanho do lado a: "))
b = float(input("Digite o tamanho do lado b: "))
c = float(input("Digite o tamanho do lado c: "))

if (a + b) < c or (a + c) < b or (b + c) < a:
    print("Estes três lado não formam um triângulo.")
elif a == b == c:
    print("Estas medidas formam um triângulo \033[34mequilátero\033[m.")
elif a == b or a == c or b == c:
    print("Estas medidas formam um triângulo \033[34misóceles\033[m.")
else:
    print("Estas medidas formam um triângulo \033[34mescaleno\033[m.")
