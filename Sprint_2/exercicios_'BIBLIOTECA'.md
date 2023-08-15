# Lista 1 de exercicios de Sql
*BANCO DE DADOS USADO*:
![Biblioteca](<DER - Biblioteca.png>)


### **E1**
Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma:

```sql 
select
    cod,
    titulo,
    autor,
    editora,
    valor,
    publicacao,
    edicao,
    idioma
from livro
where publicacao > '2014-12-31'
order by cod 
```

### **E2**
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor:

```sql
select titulo, valor
from livro
group by valor
order by valor desc
limit 10
```

### **E3**
Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente: 

```sql
select count(*) as quantidade, 
    EDITORA.nome,
    endereco.estado,
    endereco.cidade
    
from EDITORA 
    join LIVRO on EDITORA.codEditora = LIVRO.editora
    join ENDERECO on EDITORA.endereco = ENDERECO.codEndereco
group by EDITORA.nome, endereco.estado, endereco.cidade 
order by quantidade desc
limit 5
```

### **E4**
Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria):

```sql
select
    AUTOR.nome,
    AUTOR.codAutor,
    AUTOR.nascimento,
    coalesce(count(LIVRO.autor), 0) as quantidade
from
    AUTOR 
left join
    LIVRO on AUTOR.codAutor = LIVRO.autor
group by
    AUTOR.codAutor, AUTOR.nascimento, AUTOR.nome
order by
    AUTOR.nome
```
### **E5**
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno:

```sql
select distinct AUTOR.nome
        
from AUTOR
        left join LIVRO on AUTOR.codAutor = LIVRO.autor
        left join EDITORA on LIVRO.editora = EDITORA.codEditora 
        left join ENDERECO on EDITORA.endereco = ENDERECO.codEndereco
        
where ENDERECO.estado not in ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
order by AUTOR.nome
```
### **E6**
Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes:

```sql
select  AUTOR.codAutor, 
        AUTOR.nome,
        count(*) as quantidade_publicacoes
from LIVRO join AUTOR 
            on LIVRO.autor = AUTOR.codAutor
group by AUTOR.codAutor, AUTOR.nome
order by quantidade_publicacoes desc
limit 1
```
### **E7**
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente:

```sql
select AUTOR.nome

from AUTOR left join LIVRO 
            on AUTOR.codAutor = LIVRO.autor 
where LIVRO.autor is null
order by AUTOR.nome
```