import csv

tabela_periodica = {}
estados = {
            'l' : 'Líquido', 
            'g' : 'Gasoso',
            's' : 'Sólido',
            'd' : 'Desconhecido'
        }

arquivo = csv.reader(open('baseDeDados.txt'), delimiter=';')
for i,dado_linha in enumerate(arquivo):
    if i == 0: # pula linha do cabecalho (1º linha do arquivo)
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0] # Simbolo
    dados['nome'] = dado_linha[1] # Nome    
    dados['nAtomico'] = dado_linha[2] # Número Atômico
    dados['linha'] = dado_linha[3] # Linha do elemento
    dados['coluna'] = dado_linha[4] # Coluna do elemento
    dados['estado'] = estados[dado_linha[5]] # Estado da matéria

    # insere os dados na tabela periodica
    tabela_periodica[dados['simbolo']] = dados

# Busca elemento pelo simbolo     
    def buscaPorElemento():
        print('Elemento: ')
        elementoPesquisa = input()
        elemento = tabela_periodica[elementoPesquisa]
        print("--------")
        print("Símbolo: " + elemento['simbolo'])
        print("Nome: " + elemento['nome'])
        print("Número atômico: " + elemento['nAtomico'])
        print("Linha: " + elemento['linha'])
        print("Coluna: " + elemento['coluna'])
        print("Estado da matéria: " + elemento['estado'])

    def listaNomes():
        for j,dado_coluna in enumerate(arquivo):
            if j == 0: # pula linha do cabecalho (1º linha do arquivo)
                continue
            print(elemento['nome'])

    # Busca elemento pelo simbolo     
    def listaElementosCompleto():
        for l,dado_coluna in enumerate(arquivo):
            if l == 0:
                continue 
            elemento['nome']
            elemento = tabela_periodica[elemento]
            print("--------")
            print("Símbolo: " + elemento['simbolo'])
            print("Nome: " + elemento['nome'])
            print("Número atômico: " + elemento['nAtomico'])
            print("Linha: " + elemento['linha'])
            print("Coluna: " + elemento['coluna'])
            print("Estado da matéria: " + elemento['estado'])

    def menu():
        print("> 1 < Listar todos os elementos\n")
        print("> 2 < Listar todos os elementos(completo)\n")
        print("> 3 < Buscar por símbolo")
        opMenu = input()
        switch(opMenu){
            case 1: listaNomes()
                    break
            case 2: print("Aqui ainda não carai")
                    break
            case 3: buscaPorElemento()
                    break
        }
menu()





