import csv

tabela_periodica = {}
estados = {'l': 'Líquido', 'g': 'Gasoso'}

arq = csv.reader(open('tabela.txt'), delimiter=';')
for i,dado_linha in enumerate(arq):
    if i == 0: # pula linha do cabecalho (1a linha do arquivo)
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] # simbolo
    dados['nome'] = dado_linha[1] # nome    
    # demais dados
    dados['estado'] = estados[dado_linha[5]]

    # insere os dados na tabela periodica
    tabela_periodica[dados['simbolo']] = dados

# BUSCANDO PELO ELEMENTO Mercurio
print(tabela_periodica['Hg'])

# ACESSANDO OS DADOS DO ELEMENTO Hg
elemento = tabela_periodica['Hg']
print("--------")
print(elemento['simbolo'])
print(elemento['nome'])
print(elemento['estado'])









    
    
