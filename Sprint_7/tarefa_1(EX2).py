#EXERCICIO 2 : Apresente a média da coluna contendo o número de filmes.

with open("actors.csv", "r") as arquivo:
    linhas = arquivo.readlines()

linhas = linhas[1:]

numero_filmes = []

for linha in linhas:
    colunas = linha.split(',')
    if colunas[0].startswith('"'):              #gambiarra para verificar se o primeiro elemento da primeira coluna começa com' " ', evitando o erro com o ""Robert Downey, Jr.""
        Number_of_Movie = float(colunas[3])
    else:
        Number_of_Movie = float(colunas[2])

    numero_filmes.append(Number_of_Movie)

media_filmes = sum(numero_filmes) / len(numero_filmes)

print(f'A média de filmes é {media_filmes}.') 