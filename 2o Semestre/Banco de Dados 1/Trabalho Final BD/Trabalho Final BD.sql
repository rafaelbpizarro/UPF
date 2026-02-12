CREATE TABLE Usuario (
    idUser INT PRIMARY KEY,
    Nome VARCHAR(12) NOT NULL,
    Email VARCHAR(50) UNIQUE NOT NULL,
    Senha VARCHAR(30) NOT NULL
);

CREATE TABLE Jogo (
    idJogo INT PRIMARY KEY,
    Titulo VARCHAR(50) NOT NULL,
    Desenvolvedora VARCHAR(50) NOT NULL,
    Preco DECIMAL(10,2),
    Genero VARCHAR(50) NOT NULL
);

CREATE TABLE Venda (
    idVenda INT PRIMARY KEY,
    Data DATE NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    idJogo INT NOT NULL,
    FOREIGN KEY (idJogo) REFERENCES Jogo(idJogo)
);

CREATE TABLE Biblioteca (
    idBiblio INT PRIMARY KEY,
    HorasJogadas INT DEFAULT 0,
    DataAdicao DATE NOT NULL,
    idUser INT NOT NULL,
    FOREIGN KEY (idUser) REFERENCES Usuario(idUser)
);

CREATE TABLE Biblioteca_Jogo (
    idBiblio INT NOT NULL,
    idJogo INT NOT NULL,
    PRIMARY KEY (idBiblio, idJogo),
    FOREIGN KEY (idBiblio) REFERENCES Biblioteca(idBiblio),
    FOREIGN KEY (idJogo) REFERENCES Jogo(idJogo)
);

CREATE TABLE Avaliacao (
    idAv INT PRIMARY KEY,
    Data DATE NOT NULL,
    Nota INT CHECK (Nota BETWEEN 0 AND 5),
    Comentario VARCHAR(100),
    idUser INT NOT NULL,
    idJogo INT NOT NULL,
    FOREIGN KEY (idUser) REFERENCES Usuario(idUser),
    FOREIGN KEY (idJogo) REFERENCES Jogo(idJogo)
);



INSERT INTO Usuario (idUser, Nome, Email, Senha) VALUES
(1000, 'anasilva01', 'ana.silva@email.com', 'senha123'),
(1001, 'brunogames', 'bruno.costa@email.com', '123456'),
(1002, 'CarlaXD', 'carla.souza@email.com', 'abc123'),
(1003, 'diegomartins', 'diego.martins@email.com', 'qwerty'),
(1004, 'fer', 'fernanda.lima@email.com', 'senha456');

INSERT INTO Jogo (idJogo, Titulo, Desenvolvedora, Preco, Genero) VALUES
(100, 'The Witcher 3: Wild Hunt', 'CD Projekt Red', 149.90, 'RPG'),
(101, 'Counter-Strike: Global Offensive', 'Valve', 0.00, 'FPS'),
(102, 'Minecraft', 'Mojang Studios', 99.90, 'Sandbox'),
(103, 'Elden Ring', 'FromSoftware', 249.90, 'RPG'),
(104, 'FIFA 23', 'EA Sports', 299.90, 'Esporte');

INSERT INTO Venda (idVenda, Data, Total, idJogo) VALUES
(1, '2023-01-15', 149.90, 100),
(2, '2023-02-20', 0.00, 101),
(3, '2023-03-05', 99.90, 102),
(4, '2023-05-10', 249.90, 103),
(5, '2023-07-22', 299.90, 104);

INSERT INTO Biblioteca (idBiblio, HorasJogadas, DataAdicao, idUser) VALUES
(01, 120, '2023-01-16', 1000),
(02, 340, '2023-02-22', 1001),
(03, 50, '2023-03-07', 1002),
(04, 10, '2023-05-12', 1003),
(05, 200, '2023-07-23', 1004);

INSERT INTO Biblioteca_Jogo (idBiblio, idJogo) VALUES
(01, 100),
(02, 101),
(03, 102),
(04, 103),
(05, 104),
(01, 101),
(02, 102),
(03, 104),
(04, 100),
(05, 103);

INSERT INTO Avaliacao (idAv, Data, Nota, Comentario, idUser, idJogo) VALUES
(1, '2023-01-20', 5, 'Um dos melhores RPGs que já joguei!', 1000, 100),
(2, '2023-02-25', 4, 'Clássico dos FPS, sempre divertido.', 1001, 101),
(3, '2023-03-10', 3, 'Criatividade sem limites!', 1002, 102),
(4, '2023-05-15', 5, 'Obra-prima moderna dos RPGs.', 1003, 103),
(5, '2023-07-25', 3, 'Bom jogo de futebol, mas caro.', 1004, 104),
(6, '2023-02-28', 4, 'Ótimo para jogar com amigos.', 1000, 101),
(7, '2023-03-12', 5, 'Viciante!', 1001, 102),
(8, '2023-07-26', 5, 'Gráficos incríveis.', 1002, 103),
(9, '2023-01-22', 4, 'História fantástica.', 1003, 100),
(10, '2023-07-30', 3, 'Mais do mesmo.', 1004, 104);

--A Loja teve um desconto de 20% nos jogos que custam mais de 100 reais.
UPDATE Jogo
SET Preco = Preco * 0.8
WHERE Preco > 100.00;

--Estamos consultando a Avaliação de um jogo, quem a fez e o jogo que foi avaliado
SELECT 
    u.Nome AS Usuario,
    j.Titulo AS Jogo,
    a.Nota,
    a.Comentario,
    a.Data
FROM Avaliacao a
INNER JOIN Usuario u ON a.idUser = u.idUser
INNER JOIN Jogo j ON a.idJogo = j.idJogo
ORDER BY a.Nota DESC;

--Adicionamos um novo jogo, sem vendas, e com o LEFT JOIN fizemosa consulta
--dos jogos e suas vendas, como GTA VI ainda não teve vendas, seu valor é nulo 

INSERT INTO Jogo VALUES
(105, 'Grand Theft Auto VI', 'Rockstar', 1000, 'RPG');

SELECT
    j.Titulo AS Jogo,
    v.Data AS DataVenda,
    v.Total AS ValorVenda
FROM Jogo j
LEFT JOIN Venda v ON j.idJogo = v.idJogo
ORDER BY j.Titulo;

--Fizemos a média das avaliações e mostramos apenas avaliações de 4 e 5 estrelas

SELECT 
    j.Titulo AS Jogo,
    ROUND(AVG(a.Nota), 1) AS MediaNotas,
    COUNT(a.idAv) AS QtdeAvaliacoes
FROM Jogo j
INNER JOIN Avaliacao a ON j.idJogo = a.idJogo
GROUP BY j.Titulo
HAVING AVG(a.Nota) >= 4
ORDER BY MediaNotas DESC;