SELECT SYSDATE FROM DUAL;

--O drop elimina tabela, cuidado
--DROP TABLE quotes; APAGA OS DADOS E A ESTRUTURA
--O create cria a tabela
CREATE TABLE quotes (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, --cria campo id, gera numeros a partir do 1
    quote_text VARCHAR2(1000) NOT NULL,
    author_name VARCHAR2(200) NOT NULL
);

--insere uma linha na tabela
INSERT INTO quotes (quote_text, author_name) VALUES ('Ser ou não ser', 'Shakespeare');

INSERT INTO quotes (quote_text, author_name) 
VALUES ('De tudo ao meu amor serei atento', 'Vinicius de Morais');

--confirma a inserção
COMMIT;
--recupera todos campos e todas linhas da tabela
SELECT * FROM quotes;

--recuperar uma linha com o autor como Shakespeare
SELECT quote_text, author_name FROM quotes --so os campos citacao, autor
WHERE UPPER(author_name) LIKE '%SHAKE%'; --filtra o autor em maiusculo com SHAKE no nome

--apagando dados da tabela(toda tabela) APAGA SOH O CONTEUDO
DELETE FROM QUOTES; --posso me arrepender e voltar os dados com rollback
--ou
TRUNCATE TABLE QUOTES; --nao volta mais
