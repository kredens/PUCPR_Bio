create database Genes;

CREATE TABLE genoma (
id_genoma INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
arquivo VARCHAR(100) NOT NULL,
);
CREATE TABLE execucao (
id_execucao INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
id_genoma INT(11) NOT NULL,
deslocamento INT(11),
);
CREATE TABLE bloco (
id_bloco INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
id_execucao INT(11) NOT NULL,
arquivo VARCHAR(100),
);
CREATE TABLE bateria (
id_bateria INT(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
id_genoma INT(11) NOT NULL,
tamanho_bloco int(11),
);
