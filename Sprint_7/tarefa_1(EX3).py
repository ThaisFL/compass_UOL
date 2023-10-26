#EXERCICIO 3 : Apresente o ator_nome do ator/atriz com a maior média por filme.

with open("actors.csv", "r") as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

numero_filmes = {}

for linha in linhas:
    colunas = linha.split(',')
    if colunas[0].startswith('"'):          #gambiarra para verificar se o primeiro elemento da primeira coluna começa com' " ', evitando o erro com o ""Robert Downey, Jr.""
        Average_per_Movie = float(colunas[4])
    else:
        Average_per_Movie = float(colunas[3])

    if colunas[0].startswith('"'):
        actor = colunas[0].strip('"')
    else:
        actor = colunas[0]
    
    numero_filmes[actor] = Average_per_Movie     #adicionando a chave(actor) e o valor(Average_per_Movie) ao dicionario.

maior_media = max(numero_filmes.values())
ator_nome = ""

for actor, Average_per_Movie in numero_filmes.items():      #procurando o ator.
    if Average_per_Movie == maior_media:
        ator_nome = actor

print(f'O ator {ator_nome} tem a maior media de filmes, com uma media de {maior_media} filmes.')