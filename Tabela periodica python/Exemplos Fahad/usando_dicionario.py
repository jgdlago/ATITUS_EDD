# Dicionario (dict)

# Conceito de chave-valor
filmes = {} # dicionario vazio

dados_filme = {} # dicionario representando dados de filme
dados_filme['ano'] = 1985
dados_filme['genero'] = 'Ação'
dados_filme['elenco'] = ['Sylvester Stallone', 'Richard Crenna']

filmes['Rambo 2'] = dados_filme

print(filmes) # mostra o dicionario completo

# Obtem o ano do filme 'Rambo 2'
print(filmes['Rambo 2']['ano'])

# Testa se o item existe
titulo = 'Rambo 3'
if titulo in filmes:
    print(filmes[titulo])
else:
    print('Filme "{}" nao existe na base de dados.'.format(titulo))
