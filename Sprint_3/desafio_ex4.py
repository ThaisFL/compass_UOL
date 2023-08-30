#!/usr/local/bin/python3

movie_contagem = {}     #dicionario para armazenar a contagem dos filmes (key) e seus nomes (valor).

with open("actors.csv") as arquivo:
    ler_linhas = arquivo.readlines()

for linha in ler_linhas:
    colunas = linha.split(',')
    movie = colunas[4]
    
    if movie in movie_contagem:
        movie_contagem[movie] += 1      #se o movie estiver no dicionario movie_contagem entao a contagem aumenta +1
    else:
        movie_contagem[movie] = 1
    
MaxMovie_nome = max(movie_contagem, key = movie_contagem.get) #busca pela maior chave (key) no dicionario movie_contagem.

Max_Contagem = movie_contagem[MaxMovie_nome]    #busca pelo maior valor dentro do dicionario

#Novo arquivo para armazenar o resultado
num = 0
with open("movie_contagem.txt", "w") as exercicio04:
    for movie, count in movie_contagem.items():
        exercicio04.write(f"{num} - O filme '{movie}' aparece {count} vez(es) no dataset.\n")
        num = num + 1

      #A funçao 'write' escreve um texto no novo arquivo
      # A funçao 'count' ira contar quantas vezes o um 'movie' aparece como um item no dict 'movie_contagem'.