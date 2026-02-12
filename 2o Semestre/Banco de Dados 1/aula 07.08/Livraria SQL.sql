--CASO DE ESTUDO 1 BANCO DE DADOS

--Criar a tabela TEMA

		--drop table NOME_DA_TABELA (apagar tabela)
CREATE TABLE Theme(
	Code INT PRIMARY KEY,
	Description VARCHAR(20) NOT NULL
);

CREATE TABLE Book(
	ISBN INT PRIMARY KEY,
	Pages INT,
	Title VARCHAR(50),
	PublishYear VARCHAR(4),
	ThemeCode INT NOT NULL,
	FOREIGN KEY (ThemeCode) REFERENCES Theme(Code)
);

CREATE TABLE Country(
	Acronyum VARCHAR(2) PRIMARY KEY,
	CountryName VARCHAR(30) NOT NULL
);

CREATE TABLE Author(
	Code INT PRIMARY KEY,
	AuthorName VARCHAR(40) NOT NULL,
	Birthdate date,
	Email VARCHAR(50),
	CountryAcronyum VARCHAR(2),
	FOREIGN KEY (CountryAcronyum) REFERENCES Country(Acronyum)
);

CREATE TABLE BookAuthor(
	Code INT PRIMARY KEY,
	ContributionType VARCHAR(15) NOT NULL,
	AuthorCode INT NOT NULL,
	BookCode INT NOT NULL,
	FOREIGN KEY (AuthorCode) REFERENCES Author(Code),
	FOREIGN KEY (BookCode) REFERENCES Book(ISBN)
);