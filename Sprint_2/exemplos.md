# Comandos Basicos

## SELECT
> Exercicios sobre os comandos

- __(EXEMPLO 1) Seleção de uma coluna de uma tabela__
Liste os e-mails dos clientes da tabela sales.customers:

{c:gold}
select email 
from sales.customers
{/c}

- __(EXEMPLO 2) Seleção de mais de uma coluna de uma tabela__
Liste os emails e nomes dos clientes da tabela sales.customers:
{c:gold}
'select' email, first_name, last_name
'from' sales.customers
{/c}
-- (Exemplo 3) Seleção de todas as colunas de uma tabela
-- Liste todos as informações dos clientes da tabela sales.customers
select *
from sales.customers

-- RESUMO ##########################################################################
-- (1) Comando usado para selecionar colunas de tabelas
-- (2) Quando selecionar mais de uma coluna, elas devem ser separadas por vírgula 
-- sem conter vírgula antes do comando FROM
-- (3) Pode-se utilizar o asterisco (*) para selecionar todas as colunas da tabela




-- ____*____*____*____*____*____ EXERCICIO 2 - DISTINT ____*____*____*____*____*____
-- PARA QUE SERVE ##################################################################
-- Serve para remover linhas duplicadas e mostrar apenas linhas distintas
-- Muito usado na etapa de exploração das bases 


-- SINTAXE #########################################################################
select distinct coluna_1, coluna_2, coluna_3
from schema_1.tabela_1


-- EXEMPLOS ########################################################################

-- (Exemplo 1) Seleção de uma coluna sem DISTINCT
-- Liste as marcas de carro que constam na tabela products
select brand 
from sales.products

-- (Exemplo 2) Seleção de uma coluna com DISTINCT
-- Liste as marcas de carro distintas que constam na tabela products
select distinct brand
from sales.products

-- (Exemplo 3) Seleção de mais de uma coluna com DISTINCT
-- Liste as marcas e anos de modelo distintos que constam na tabela products
select distinct brand, model_year
from sales.products

-- RESUMO ##########################################################################
-- (1) Comando usado para remover linhas duplicadas e mostrar apenas linhas distintas
-- (2) Muito utilizado na etapa de exploração dos dados
-- (3) Caso mais de uma coluna seja selecionada, o comando SELECT DISTINCT irá 
-- retornar todas as combinações distintas.




-- ____*____*____*____*____*____ EXERCICIO 3 - WHERE ____*____*____*____*____*____*____
-- PARA QUE SERVE ##################################################################
-- Serve para filtrar linhas de acordo com uma condição


-- SINTAXE #########################################################################
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true


-- EXEMPLOS ########################################################################

-- (Exemplo 1) Filtro com condição única
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina
select email, state
from sales.customers
where state = 'SC'

select state
from sales.customers
-- (Exemplo 2) Filtro com mais de uma condição
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina
-- ou Mato Grosso do Sul
select email, state
from sales.customers
where state = 'SC' or state = 'MS'

-- (Exemplo 3) Filtro de condição com data
-- Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina 
-- ou Mato Grosso do Sul e que tem mais de 30 anos
select email, state, birth_date
from sales.customers
where (state = 'SC' or state = 'MS') and birth_date < '1991-12-28'

-- RESUMO ##########################################################################
-- (1) Comando utilizado para filtrar linhas de acordo com uma condição
-- (2) No PostgreSQL são utilizadas aspas simples para delimitar strings 
-- (3) string = sequência de caracteres = texto
-- (4) Pode-se combinar mais de uma condição utilizando os operadores lógicos
-- (5) No PostgreSQL as datas são escritas no formato 'YYYY-MM-DD' ou 'YYYYMMDD'






-- ____*____*____*____*____*____ EXERCICIO 4 - ORDER BY ____*____*____*____*____*____*____
-- PARA QUE SERVE ##################################################################
-- Serve para ordenar a seleção de acordo com uma regra definida pelo usuário


-- SINTAXE #########################################################################
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true
order by coluna_1


-- EXEMPLOS ########################################################################

-- (Exemplo 1) Ordenação de valores numéricos
-- Liste produtos da tabela products na ordem crescente com base no preço
select *
from sales.products
order by price

-- (Exemplo 2) Ordenação de texto
-- Liste os estados distintos da tabela customers na ordem crescente
select distinct state
from sales.customers
order by state


-- RESUMO ##########################################################################
-- (1) Comando utilizado para ordenar a seleção de acordo com uma regra definida
-- (2) Por padrão o comando ordena na ordem crescente. Para mudar para a ordem 
-- decrescente usar o comando DESC
-- (3) No caso de strings a ordenação será seguirá a ordem alfabetica





-- ____*____*____*____*____*____ EXERCICIO 5 - LIMIT ____*____*____*____*____*____*____
-- PARA QUE SERVE ##################################################################
-- Serve para limitar o nº de linhas da consulta.
-- Muito utilizado na etapa de exploração dos dados


-- SINTAXE #########################################################################
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
limit N


-- EXEMPLOS ########################################################################

-- (Exemplo 1) Seleção das N primeiras linhas usando LIMIT
-- Liste as 10 primeiras linhas da tabela funnel utilizando o LIMIT
select *
from sales.funnel
limit 10

-- (Exemplo 2) Seleção das N primeiras linhas usando LIMIT e ORDER BY
-- Liste os 10 produtos mais caros da tabela products com o comando LIMIT
select *
from sales.products
order by price desc
limit 10

-- RESUMO ##########################################################################
-- (1) Comando utilizado para limitar o nº de linhas da consulta.
-- (2) Muito utilizado na etapa de exploração dos dados
-- (3) Muito utilizado em conjunto com o comando ORDER BY quando o que importa são
-- os TOP N. Ex: "N pagamentos mais recentes", "N produtos mais caros"







