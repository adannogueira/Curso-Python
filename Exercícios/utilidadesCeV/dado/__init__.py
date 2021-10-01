# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

def leiaDinheiro(v):
	while 1:
		valor = input(v).strip()
		try:
			valor = float(valor.replace(',', '.'))
			break
		except ValueError:
			print(f'ERRO: \"{valor}\" é um preço inválido.')
			continue
	return valor

