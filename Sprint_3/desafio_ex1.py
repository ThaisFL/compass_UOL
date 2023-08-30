#!/usr/local/bun/python3

with open("actors.csv", "r") as arquivo:
    ler_linhas = arquivo.readlines()

ler_linhas = ler_linhas[1:]

numero_filmes = 0
ator_filme = ''

for linha in ler_linhas:
    colunas = linha.split(',')
    Number_of_Movies =  float(colunas[2])
    if Number_of_Movies >= numero_filmes:
        numero_filmes = Number_of_Movies
        ator_filme = colunas[0]

print(f'O ator {ator_filme} tem {numero_filmes} filmes entao ele é o que fez mais filmes dentre todos.')




