# Comandos Basicos
> Exercicios resolvidos sobre cada um dos comandos basicos

## SELECT
- __(EXEMPLO 1) Seleção de uma coluna de uma tabela__
1. *Liste os e-mails dos clientes da tabela sales.customers:*
```
\_select\_ email 
\_from\_ sales.customers

```
---

- __(EXEMPLO 2) Seleção de mais de uma coluna de uma tabela__
2. *Liste os emails e nomes dos clientes da tabela sales.customers:*

\_*select*\_ email, first_name, last_name
\_*from*\_ sales.customers

---

- __(EXEMPLO 3) Seleção de todas as colunas de uma tabela__
3. *Liste todos as informações dos clientes da tabela sales.customers:*

\_*select* *\_ 
\_*from*\_ sales.customers

---


## DISTINT
- __(EXEMPLO 1) Seleção de uma coluna sem DISTINCT__
1. *Liste as marcas de carro que constam na tabela products:*

\_*select*\_brand
\_*from*\_ sales.products

---

- __(EXEMPLO 2) Seleção de uma coluna com DISTINCT__
2. *Liste as marcas de carro distintas que constam na tabela products:*

\_*select\_\_distinct*\_ brand
\_*from*\_ sales.products

---

- __(EXEMPLO 3) Seleção de mais de uma coluna com DISTINCT__
3. *Liste as marcas e anos de modelo distintos que constam na tabela products:*

\_*select\_\_distinct*\_ brand, model_year
\_*from*\_ sales.products

---


## WHERE
- __(EXEMPLO 1) Filtro com condição única:__
1. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina:*

\_*select*\_ email, state
\_*from*\_ sales.customers
\_*where*\_ state = 'SC'

---

- __(EXEMPLO 2) Filtro com mais de uma condição__
2. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina ou Mato Grosso do Sul:*

\_*select*\_ email, state
\_*from*\_ sales.customers
\_*where*\_ state = 'SC' \_*or*\_ state = 'MS'

---

- __(EXEMPLO 3) Filtro de condição com data__
3. *Liste os emails dos clientes da nossa base que moram no estado de Santa Catarina ou Mato Grosso do Sul e que tem mais de 30 anos:*

\_*select*\_ email, state, birth_date
\_*from*\_ sales.customers
\_*where*\_ (state = 'SC' \_*or*\_ state = 'MS') \_*and*\_ birth_date < '1991-12-28'

---


## ORDER BY
- __(EXEMPLO 1) Ordenação de valores numéricos__
1. *Liste produtos da tabela products na ordem crescente com base no preço:*

\_*select*\_ * 
\_*from*\_ sales.products
\_*order by*\_ price

---

- __(EXEMPLO 2) Ordenação de texto__
2. *Liste os estados distintos da tabela customers na ordem crescente:*

\_*select*\_ distinct state
\_*from*\_ sales.customers
\_*order by*\_ state

---


## LIMIT
- __(EXEMPLO 1) Seleção das N primeiras linhas usando LIMIT__
1. *Liste as 10 primeiras linhas da tabela funnel utilizando o LIMIT:*

\_*select*\_ *
\_*from*\_ sales.funnel
\_*limit*\_ 10

---

- __(EXEMPLO 2) Seleção das N primeiras linhas usando LIMIT e ORDER BY__
2. *Liste os 10 produtos mais caros da tabela products com o comando LIMIT:*

\_*select*\_ *
\_*from*\_ sales.products
\_*order by*\_ price \_*desc*\_
\_*limit*\_ 10

---

## __D E S A F I O__
1. *(Exercício 1) Selecione os nomes de cidade distintas que existem no estado de Minas Gerais em ordem alfabética (dados da tabela sales.customers):*

\_*select*\_ distinct city
\_*from*\_ sales.customers
\_*where*\_ state = 'MG'
\_*order by*\_ city

---

2. *(Exercício 2) Selecione o visit_id das 10 compras mais recentes efetuadas (dados da tabela sales.funnel):*

\_*select*\_ visit_id
\_*from*\_ sales.funnel
\_*where*\_ paid_date \_*is not null*\_
\_*order by*\_ paid_date \_*desc*\_
\_*limit*\_ 10

---

3. *(Exercício 3) Selecione todos os dados dos 10 clientes com maior score nascidos após 01/01/2000 (dados da tabela sales.customers):*

\_*select*\_ *
\_*from*\_ sales.customers
\_*where*\_ birth_date > '2000/01/01'
\_*order by*\_ score \_*desc*\_
\_*limit*\_ 10

---
