#!/usr/local/bin/python3
# Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados.
# Considere a coluna Avarage per Movie para fins de cálculo.

with open("actors.csv", "r") as arquivo:
    ler_linhas = arquivo.readlines()

ler_linhas = ler_linhas[1:]

lista_Avarage = []                #criando uma lista para armazenar o Avarage_Movie 

for linha in ler_linhas:
    colunas = linha.split(',')
    if colunas[0].startswith('"'):      #gambiarra para verificar se o primeiro elemento da primeira coluna começa com' " '
        Avarage_Movie  = float(colunas[4])
    else:
        Avarage_Movie  = float(colunas[3])  

    lista_Avarage.append(Avarage_Movie )
    
media = sum(lista_Avarage) / len(lista_Avarage)

print(media)
