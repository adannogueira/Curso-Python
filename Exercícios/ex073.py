# Crie uma TUPLA preenchida com os vinte primeiros colocados  da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados.
# c) Uma LISTA com os times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Corinthians',
         'Bragantino', 'Santos', 'Athletico-PR', 'Atlético-GO', 'Ceará', 'Sport', 'Fortaleza', 'Bahia', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')

print(f'Os cinco primeiros colocados são {times[0:5]}')
print(f'Os quatro últimos colocados são {times[-4:]}')
print(f'Em ordem alfabética os times são {sorted(times)}')
if times.count('Chapecoense') == False:
    print('A Chapecoense não está na lista.')
else:
    print(f'A Chapecoense está em {times.index("Chapecoense") + 1}º lugar.')