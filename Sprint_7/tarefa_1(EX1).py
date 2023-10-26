# EXERCICIO 1 : Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes. 


import pandas as pd
import numpy as np

# Carregando o arquivo CSV em um DataFrame
df = pd.read_csv("actors.csv")

# Corrigindo nomes dos atores/atrizes com aspas duplas no início e no fim
df['Actor'] = df['Actor'].str.strip('"')

# Calculando a média de filmes por ator/atrizes
df['Average_per_Movie'] = np.where(df['Actor'].str.startswith('"'), df['Gross % US'], df['Gross % US.1']).astype(float)

# Encontrando o ator/atrizes com o maior número de filmes
ator_com_mais_filmes = df.loc[df['Average_per_Movie'].idxmax()]

print(f'O ator {ator_com_mais_filmes["Actor"]} foi o ator que mais participou de filmes, no total foram {ator_com_mais_filmes["Average_per_Movie"]:.2f} filmes feitos.')



#RESULTADO: 


#-------------------------------------------------------------------------------------


with open("actors.csv", "r") as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

list_filmes = {}     #lista para armazenar o numero de filmes

for linha in linhas: #implementando a lista "numero_filmes"
    colunas = linha.split(',')
    if colunas[0].startswith('"'):                      #gambiarra para verificar se o primeiro elemento da primeira coluna começa com' " ', evitando o erro com o ""Robert Downey, Jr.""
        Numero_Filmes = float(colunas[3])
    else:
        Numero_Filmes = float(colunas[2])

    if colunas[0].startswith('"'):
        actor = colunas[0].strip('"')
    else:
        actor = colunas[0]

    list_filmes[actor] = Numero_Filmes #adicionando a chave (actor) e o valor (number of movies) ao dicionario.

maior_numero = max(list_filmes.values())
ator_nome = ""

for actor, Numero_Filmes in list_filmes.items(): #procurando o nome do ator.
    if Numero_Filmes == maior_numero:
        ator_nome = actor

print(f'O ator {ator_nome} foi o ator que mais participou de filmes, no total foram {maior_numero} filmes feitos.')

