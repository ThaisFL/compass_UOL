#!/usr/local/bin/python3
# Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. 
# Estamos falando aqui da média da coluna Gross.

with open("actors.csv", "r") as arquivo:
    ler_linhas = arquivo.readlines()

ler_linhas = ler_linhas[1:]

Gross_lista = []   #criando uma lista para armazenar a tabela Gross.                   

for linha in ler_linhas:
    colunas = linha.split(',')

    if colunas[0].startswith('"'):      #gambiarra para verificar se o primeiro elemento da primeira coluna começa com' " '
        Gross = float(colunas[6])
    else:
        Gross = float(colunas[5])    

    Gross_lista.append(Gross) #armazenando a tabela Gross na list Gross_lista.
    
media = sum(Gross_lista) / len(Gross_lista)

print(media)