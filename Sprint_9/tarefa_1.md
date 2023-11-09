### **Tabelas**
```SQL
--CRIANDO TABELA 'CLIENTES'
CREATE TABLE clientes (
    idCliente int primary key,
    nomeCliente varchar(100),
    cidadeCliente varchar(40),
    estadoCliente varchar(40),
    paisCliente varchar(40),
    FOREIGN KEY (idCliente) REFERENCES tb_locacao(idCliente)
);
--inserindo os dados das colunas da tabela tb_locacao á tabela clientes:
INSERT INTO clientes(idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente 
FROM tb_locacao;

----------------------------
--CRIANDO TABELA 'LOCACAO'
CREATE TABLE locacao (
    idLocacao int primary key,
    dataLocacao datetime,
    horaLocacao datetime,
    qtdDiaria int,
    vlrDiaria decimal(18,2),
    dataEntrega datetime,
    horaEntrega datetimE,
        FOREIGN key (idLocacao) references tb_locacao(idLocacao) 
);
--inserindo os dados das colunas da tabela 'tb_locacao' á tabela 'locacao':
INSERT INTO locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria,  dataEntrega, horaEntrega)
SELECT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria,  dataEntrega, horaEntrega 
FROM tb_locacao;


----------------------------
--CRIANDO TABELA 'CARROS'
CREATE TABLE carros (
    idCarro int primary key,
    kmCarro int, 
    classiCarro varchar(50),
    marcaCarro varchar(80),
    modeloCarro varchar(80),
    anoCarro int,
    tipoCombustivel varchar(20),
    FOREIGN KEY (idCarro) REFERENCES tb_locacao(idCarro)
);
--inserindo os dados das colunas da tabela 'tb_locacao' á tabela 'CARROS':
INSERT INTO carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel
FROM tb_locacao;



---------------------------
--CRIANDO TABELA 'vendedor'
CREATE TABLE vendedor (
    idVendedor int primary key,
    nomeVendedor varchar(100),
    sexoVendedor smallint,
    estadoVendedor varchar(40),
    FOREIGN KEY (idVendedor) REFERENCES tb_locacao(idVendedor)
);

--inserindo as dados das colunas da tabela 'tb_locacao' á tabela 'vendedor':
INSERT INTO vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor  
FROM tb_locacao;
```
