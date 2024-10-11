CREATE DATABASE localcmd
USE localcmd

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    funcao VARCHAR(100) NOT NULL
)

CREATE TABLE users_homol(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    funcao VARCHAR(100) NOT NULL
)

SELECT * FROM users
SELECT * FROM users_homol
SELECT usuario FROM users_homol WHERE funcao = 'comum'
DELETE FROM users_homol WHERE id = 1 OR id = 2