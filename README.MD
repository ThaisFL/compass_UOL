# Compass_UOL
> Este arquivo contem o resumo apenas com as informaçoes principais e mais importantes do que foi aprendido nas sprints.

## APRESENTAÇAO
Olá, me chamo Thais tenho 17 anos e moro em Tres Lagoas-MS. Estou no 2 semestre de Sistemas de Informaçao na UFMS de Tres Lagoas. Entrei na area do TI com 0 experiência, por isso estou buscando novas experiências e aprendizagens para descobri qual area eu me dou melhor e o estagio é uma otima oportunidade de começar.

# SPRINT 1 
## Git e GitHUB
Aqui esta um resumo apenas com as informaçoes principais do que foi aprendido na sprint. Primeiramente nas aulas aprendemos a instalar o Git no windows e linux e mecher com o terminal do VS CODE. Eu estou usando o Git no windows e a maquina do VS CODE.

__*O QUE É GIT?*__ É o sistema de controle de versao mais usado no mundo atualmente, usado para controle e < organizaçao de arquivos no desenvolvimento de um projeto. Baseado em repositorios para conter codigos e copias do desenvolvedor.

> Os repositórios iniciam o projeto e armazenam os codigos; exemplos de repos muito utilizados: GitHub e Bitbucket.

__*O QUE É GITHUB?*__  É um serviço usado para gerenciar os repositórios de projetos.


__*COMANDOS PRINCIPAIS DE UM REPO NO GIT:*__
- __`git init`__ - criar repositorio.
- __`git add`__  - adicionar arquivos ao repositorio.
- __`git commit`__ - salvar alteraçoes.
    * com a tag **`-a`** ele salva varios arquivos e **`-m`** envia uma mensagem;

- __`git push`__- envia as alteraçoes ao github.
- __`git status`__- Verifica mudanças no projeto.
- __`git pull`__- Envia as mudanças do repo local para o remoto.
- __`git rm`__- remove arquivo.
- __`git clone`__- baixa um repo do git hub e clona na maquina.

## Branches
**_O QUE É UMA BRANCH?_**
É uma ramificaçao do projeto, serve para consertar bugs e inserir funçoes sem intervir no projeto principal.

**_COMANDOS PRINCIPAIS DE UMA BRANCH:_**
- __`git branch<nome>`__- criar uma nova branch.
- __`git branch -d <nome>`__- deletar branch.
- __`git pull`__- receber atualizações do repositório remoto; (atualizar o branch sempre que for usar).
- __`git checkout <nome>`__- alternar a branch.
- __`git push`__- enviar alterações mas apenas de arquivos commitados.

## Markdown
Markdown é uma forma de adicionar estilo a textos.
    ex: “README.md”; o “.md” determina uma extensao markdown.

Essa extensão permite a exibição de código, links, imagens, textos, etc. 

## LINUX
**_Por que utilizar o linux?_** O linux é usado na maioria dos servidores web, sendo usado por grandes empresas como AWS e Heroku.

**_Distribuição do linux:_** versão do linux.
*   EX: Ubuntu.

**_Kernel:_** é o core do sistema.
É o componente principal do sistema pois estabelece a comunicação entre o hardware e os processos executados pelo computador.

**_Terminal:_** basicamente uma tela do ubuntu que executa o shell.

**_COMANDOS FUNDAMENTAIS DO LINUX:_**
- __`ls`__- informa os diretórios/arquivos e seus conteúdos;
    * __`ls -l`__: mostra todos os arquivos e pastas em detalhes;
    * __`l -R`__: todos os diretórios e seus arquivo;

- __`cd <diretório>`__- mudar de diretório;
    * __`cd /`__: informa todos os diretórios disponíveis na raiz;

- __`clear`__: limpa a tela do terminal;

- __`cat`__: conteúdo de um arquivo;

- __`touch`__: muda a hora de atualização do arquivo e/ou criar arquivo vazio; 

- __`man <comando>`__: manual de um comando;

- __`mkdir <nome do diret.>`__: criar novo diretório; 

- __`rm -dv`__: remove diretório vazio;
    * __`rm -rfv`__: remove diretórios com arquivos dentro;
    * __`rmdir`__: remove apenas diretórios do sistema;

- __`cp <diret>`__: copiar diretórios;

- __`mv <arq> <diret>`__: mudar o arquivo de diretório ou renomear;

- __`pwd`__: informa o diretório onde você está;


# SPRINT 2

> **diagrama (schemas)**:  representação gráfica das tabelas do banco de dados.
> **strings**: sequência de caractere ( texto); delimitado por aspas simples.
configuração da máquina: 


## __COMANDOS BÁSICOS__

__`select`__ : selecionar as colunas de tabelas;
ex: select coluna_1, coluna_2, coluna_3

* __`select` *__ : selecionar todas as colunas da tabela.

__`distinct`__ : remove linhas duplicadas, deixando as linhas distintas.
> Caso mais de uma coluna selecionada o comando distinct irá combinar as informações das colunas para definir as linhas distintas.

__`where`__`: filtrar as linhas da tabela de acordo com uma condição. ( = , < , > )

__`or`__ : filtrar uma condição ou outra.
__`and`__: adicionar condição.
__`is not null`__ : exclui campos vazios.

__`order by`__: ordenar a seleção com base em uma regra do usuário.

__`desc`__ : Ordem decrescente.

__`limit`__ : limitar o número de linhas da consulta.

### *OPERADORES ARITMÉTICOS*
> servem para executar operações matemáticas.

__*__*Tipos*__:*__ ` * ` , ` - ` , ` + ` , ` / ` ,` ^ `, ` % ` 
` | | ‘ ‘ | | `- soma de string.


__`current_date`__: data de hj.

__`as`__ : nomear a nova coluna que mostrará o resultado da operação;


### *OPERADORES COMPARAÇÃO*
>Servem para comparar dois valores retornando TRUE ou FALSE

__*Tipos*__: ` = ` , ` > ` ,` <  `, ` >= ` , ` <= ` ,` <> `


### *OPERADORES LÓGICOS*
> Usados para unir expressões simples em uma expressão composta

__*Tipos*__: AND , OR , NOT , BETWEEN , IN , LIKE , ILIKE , IS NULL

`BETWEEN` -  define um intervalo entre dois elementos, da a resposta “TRUE” se o operando estiver dentro do intervalo.
* `not between` - TRUE se o operando não estiver entre o intervalo.

`IN` -  informa os operandos iguais a pelo menos uma das condições.
not in - não seleciona nenhum dos operandos que se igualam as condições.

`LIKE` - verifica se os operandos correspondem ao padrão.
`%` - informa que depois ou antes da seleção pode conter qualquer outra sequência de caracteres.

* `ILIKE` - ignora se a seleção está com letras maiúsculas ou minúsculas.


`IS NULL` - determina espaços nulos na tabela.
not is null - ignora os campos nulos.


## FUNÇÕES AGREGADAS
> servem para executar operações aritméticas nos registros de uma coluna e ignoram os NULL.

__*tipos*__:  COUNT()  ,  SUM()  ,   MIN()  ,  MAX()  ,  AVG()


`COUNT` - contagem do elemento selecionado
	ex: count(coluna) 
count(*) - contagem de todas as linhas. 
count(distinct <coluna>) - contagem distinta.

`MIN` - calcula o valor mínimo de uma coluna
`MAX` - calcula o valor máximo de uma coluna
`AVG` - calcula a média de uma coluna.


## GROUP BY
> servem para agrupar registros semelhantes de uma coluna. Ele desconsidera os NULL.
> normalmente usados juntos com as funçoes agregadas

`HAVING`: Serve para filtrar as linhas de uma seleção por uma coluna agrupada.
*  O where não roda com funções agregadas, portanto usa-se o having.

## **JOINS**

* `LEFT JOIN`- permite obter todos os dados relacionados de duas tabelas e os dados da tabela 1(a esquerda):

* `INNER JOIN` - permite obter apenas os dados relacionados das tabelas:

* `RIGHT JOIN` - obtém todos os dados da tabela 2(a direita) e os dados relacionados das duas:

* `FULL JOIN` - todos os dados das tabelas e o relacionado:

![exemplos joins](https://www.google.com/url)


## **TIPOS DE UNION**- usado para juntar os registros de uma ou mais tabelas.

* `UNION` - remove linhas duplicadas quando junta as duas tabelas, deixando apenas as linhas que existem em apena uma tabela:

* `UNION ALL` -  nao remove linhas duplicadas quando as tabela são unidas, ele vai só juntar o conteúdo das duas tabelas: 

![exemplos union e union all](https://www.google.com/url)

exemplo na prática, juntando duas tabelas: 
``` sql
select * from sales.products
union all
select * from temp_tables.products_2
```

## **SUBS QUERYS**

> servem para consultar dados de outras consultas, sao instruçoes do tipo SELECT dentro de outra.

tipos: WHERE ,  WITH , FROM , SELECT

Sub query no `WHERE` - SELECT dentro do where mas que retorna apenas 1 dados.

sub query no `WITH` - mais recomendável usar. comando with antes de todas as instruções,
 dessa forma: with < tabela > as ( < sub instrução> ).

sub query no `FROM` - select dentro do from com o complemento ‘as‘ para nomear a subquery.

sub query no `SELECT` - sub query dentro da declaração de tabela no select, junto do complemento ‘as‘ e entre parênteses. É uma subquery muito pesada por isso não é recomendável. E só devolve 1 dados.


## TRATAMENTOS DE DADOS

CONVERSÃO DE UNIDADES: CAST() ou :: 
> converte as instruções.

__:: date__ - converter em data
__:: numeric__ - converter em número
__::text__ - converter em text

__cast(< elemento > as date)__

### TRATAMENTO GERAL: 
> CASE WHEN e COALESCE()

`case` - é um comando usado para definir condições que serão testadas durante a execução do código, e caso alguma seja atendida, e devolve um resultado.
*	`when` - define a condição que será testada;
*	`then` - indica o resultado da condição caso será verdadeira;
*	`else` - caso nenhuma das condições sejam verdadeiras;
*	`end` - fechamento da case (pode usar um as junto, ex ‘end as’);

`coalesce()` - avalia e retorna o primeiro campo que não seja null, e preenche o campo nulo com a informação que você colocar depois da ‘,’no comando.
*ex:* 
```sql 
select 
	*,
	coalesce (population, (select avg(population) from temp_tables.regions)) as populaçao_ajustada
```

### TRATAMENTO DE TEXTO: 
> upper, lower, trim e replace

> modifica um elemento da comparação para que o resultado seja igual a TRUE.

`lower` -  utilizado para transformar todo texto em letras minúsculas;
`upper` - utilizado para transformar todo texto em letras maiúsculas;
`trim` -  utilizado para remover os espaços das partes de um texto;
`replace` - substitui uma sequência de caracteres.

### TRATAMENTO DE DATAS
> tratar dados de data e hora.

`interval` - usado para somar datas na unidade deseja. caso a unidadexnao seja informada, o SQL entende que a soma foi feita em dias.

`date_trunc` - utilizado p/ truncar uma data no início do período (retorna o primeiro dia daquele mes). Retorna uma data truncada pra um datepart especifico

`extract` - utilizado para extrair unidades de uma data/timestamp( domingo = 0, segunda = 1, terça = 2, etc…)

>*calcular a diferença entre datas* = ‘-’
>*resultado em semanas* = /7
>*resultado em meses* = /30
>*resultado em anos* = /365

### **FUNÇÕES** - comandos personalizados.

`datediff` = função para calcular a diferença entre duas datas.

`deletar função` = drop function datediff

## TABELAS 
 
**CRIAR TABELAS**: comando `into` antes do comando `from`
```sql
into < schema >.<nome nova tabela>
```

**CRIAR TABELAS DO ZERO**: comando create table`.

```sql
create table < schema >< nome tabela >(
< coluna1, tipo > , < coluna2, tipo >
)
```

**DELETAR TABELAS**: comando ´drop table´.
```sql
drop table <schema>.<tabela>
```

**ATUALIZAR LINHA**: 
```sql
update <schema.tabela>
set <coluna> = ‘<atualização>’
where <coluna e linha para atualizar>
```

**DELETAR LINHA**:
```sql
delete from <schema.tabela>
where <coluna. = <linha p deletar>
or <coluna>= <linha p deletar>
```

**ADICIONAR LINHAS**: comando insert into e values.
```sql
insert into <schema>.<tabela>
(<coluna1,coluna2>)
```

**INSERIR COLUNA**:
```sql 
alter table <schema.tabela>
add <coluna nova; tipo de unidade> 
```

**ALTERAR O TIPO DA COLUNA:**
```sql 
alter table <schema.tcabeka>
alter column <coluna> type <tipo de unidade>
```

**ALTERAR O NOME DA COLUNA**:
```sql 
alter table <schema.tabela>
rename column<coluna> to <nome novo>
```

**DELETAR COLUNA**:
```sql alter table <schema.tabela> 
drop column <coluna>
```

> fontes usadas:
>https://portal.revendadesoftware.com.br
>https://markdown.net.br/sintaxe-basica/#:~:text=T%C3%ADtulos,Todo%20documento
>https://www.w3schools.com/sql/sql_null_values.asp#:~:text=O%20que%20%C3%A9%20um%20valor%20NULO%3F 



# CERTIFICADOS 

[Certificado Git e GitHub](https://udemy-certificate.s3.amazonaws.com/image.jpg)

[Certificado LINUX](https://udemy-certificate.s3.amazonaws.com/image.jpg)

[Certificado data e analitycs 1](https://udemy-certificate.s3.amazonaws.com/image.jpg) 

[Certificado SQL para analise de dados](https://udemy-certificate.s3.amazonaws.com/image.jpg)