CREATE DATABASE teste;
USE teste;

CREATE TABLE tabela (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

INSERT INTO tabela(nome, descricao) VALUES ("Item 1", "Descrição do item 1");
INSERT INTO tabela(nome, descricao) VALUES ("Item 2", "Descrição do item 2");
INSERT INTO tabela(nome, descricao) VALUES ("Item 3", "Descrição do item 3");
INSERT INTO tabela(nome, descricao) VALUES ("Item 4", "Descrição do item 4");

SELECT * FROM tabela;