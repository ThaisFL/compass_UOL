#  Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes 
# (coluna Total Gross), em ordem decrescente.
# Ao escrever no arquivo, considere o padrão de saída 
#  <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.

with open("actors.csv") as arquivo:
    ler_linhas = arquivo.readlines()

dados = []

for linha in ler_linhas:
    colunas = linha.split(',')
    nome_ator = colunas[0]
    receita_bruta = colunas[5]

    dados.append((nome_ator,receita_bruta))
    
with open("ReceitaBruta_Atores.txt", "w") as exercicio05:
    for nome_ator, receita_bruta in dados:
        exercicio05.write(f"{nome_ator} - {receita_bruta} \n")



#Nao consegui tranformar em ordem DECRESCENTE