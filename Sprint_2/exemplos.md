# Comandos Basicos
> Exercicios resolvidos sobre cada um dos comandos basicos

## SELECT
- __(EXEMPLO 1) Seleção de uma coluna de uma tabela__
1. *Liste os e-mails dos clientes da tabela sales.customers:*

[_select_ email 
_from_ sales.customers]

---

- __(EXEMPLO 2) Seleção de mais de uma coluna de uma tabela__
2. *Liste os emails e nomes dos clientes da tabela sales.customers:*

*select* email, first_name, last_name
*from* sales.customers

---

- __(EXEMPLO 3) Seleção de todas as colunas de uma tabela__
3. *Liste todos as informações dos clientes da tabela sales.customers:*

*select* *
*from* sales.customers

---


## DISTINT
- __(EXEMPLO 1) Seleção de uma coluna sem DISTINCT__
1. *Liste as marcas de carro que constam na tabela products:*

*select*brand
*from* sales.products

---

- __(EXEMPLO 2) Seleção de uma coluna com DISTINCT__
2. *Liste as marcas de carro distintas que constam na tabela products:*

*select distinct* brand
*from* sales.products

---

- __(EXEMPLO 3) Seleção de mais de uma coluna com DISTINCT__
3. *Liste as marcas e anos de modelo distintos que constam na tabela products:*

*select distinct* brand, model_year
*from* sales.products

---


## WHERE
- __(EXEMPLO 1) Filtro com condição única:__
1. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina:*

*select* email, state
*from* sales.customers
*where* state = 'SC'

---

- __(EXEMPLO 2) Filtro com mais de uma condição__
2. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina ou Mato Grosso do Sul:*

*select* email, state
*from* sales.customers
*where* state = 'SC' *or* state = 'MS'

---

- __(EXEMPLO 3) Filtro de condição com data__
3. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina ou Mato Grosso do Sul e que tem mais de 30 anos:*

*select* email, state, birth_date
*from* sales.customers
*where* (state = 'SC' *or* state = 'MS') *and* birth_date < '1991-12-28'

---


## ORDER BY
- __(EXEMPLO 1) Ordenação de valores numéricos__
1. *Liste produtos da tabela products na ordem crescente com base no preço:*

*select* * 
*from* sales.products
*order by* price

---

- __(EXEMPLO 2) Ordenação de texto__
2. *Liste os estados distintos da tabela customers na ordem crescente:*

*select* distinct state
*from* sales.customers
*order by* state

---


## LIMIT
- __(EXEMPLO 1) Seleção das N primeiras linhas usando LIMIT__
1. *Liste as 10 primeiras linhas da tabela funnel utilizando o LIMIT:*

*select* *
*from* sales.funnel
*limit* 10

---

- __(EXEMPLO 2) Seleção das N primeiras linhas usando LIMIT e ORDER BY__
2. *Liste os 10 produtos mais caros da tabela products com o comando LIMIT:*

*select* *
*from* sales.products
*order by* price *desc*
*limit* 10

---

## __D E S A F I O__
1. *(Exercício 1) Selecione os nomes de cidade distintas que existem no estado de Minas Gerais em ordem alfabética (dados da tabela sales.customers):*

*select* distinct city
*from* sales.customers
*where* state = 'MG'
*order by* city

---

2. *(Exercício 2) Selecione o visit_id das 10 compras mais recentes efetuadas (dados da tabela sales.funnel):*

*select* visit_id
*from* sales.funnel
*where* paid_date *is not null*
*order by* paid_date *desc*
*limit* 10

---

3. *(Exercício 3) Selecione todos os dados dos 10 clientes com maior score nascidos após 01/01/2000 (dados da tabela sales.customers):*

*select* *
*from* sales.customers
*where* birth_date > '2000/01/01'
*order by* score *desc*
*limit* 10

---
