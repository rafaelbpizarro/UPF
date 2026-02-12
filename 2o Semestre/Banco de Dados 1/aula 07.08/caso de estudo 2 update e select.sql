--  Aumentar o salário em 10% de todos os funcionários que recebem menos de 2000
UPDATE Funcionario
SET salario = salario * 1.10
WHERE salario < 2000;

-- Atualizar o endereço de um cliente específico
UPDATE Cliente
SET endereco = 'Rua Nova Central, 1500'
WHERE codCliente = 3;

--  Alterar a quantidade em estoque de um produto após reposição de 50 unidades
UPDATE Produto
SET qtdEstoque = qtdEstoque + 50
WHERE codProduto = 7;

-- WHERE com operadores lógicos: produtos com preço maior que 100 e estoque acima de 20
SELECT * FROM Produto
WHERE valorUnitario > 100 AND qtdEstoque > 20;

--IS NULL: listar o nome dos clientes sem telefone
SELECT nome FROM Cliente
WHERE telefone IS NULL;

---- BETWEEN: listar o PRODUTO e o PREÇO cujo preço está entre 50 e 200
SELECT descricao, valorUnitario FROM Produto
WHERE valorUnitario BETWEEN 50 AND 200;

-- EXTRACT de datas: selecionar pedidos feitos em 2024
SELECT * FROM Pedido
WHERE EXTRACT(YEAR FROM dataEntrega) = 2024;

-- LIKE: buscar clientes cujo nome começa com 'M'
SELECT * FROM Cliente 
WHERE nome LIKE 'M%';


-- LIKE: buscar produtos que contenham 'Cimento' na descrição
SELECT * FROM Produto
WHERE descricao LIKE '%Cimento%';


-- ============= EXERCICIOS =============
-- 1) Modifique o endereço de um cliente 'Thiago Ramos' para "Av. Brasil, 999".
UPDATE Cliente
SET endereco = 'Av. Brasil, 999'
WHERE nome = 'Thiago Ramos';

-- 2) Diminua em 2 unidades o estoque do produto 'Trena 5m'

UPDATE Produto
SET qtdestoque = qtdestoque - 2
WHERE codproduto = 227;

-- 3) Atualize o salário dos funcionários da empresa 'Construmax', com salário abaixo de 2500, aumentando em 15%.

SELECT * from funcionario where codempresa = 4 and salario < 2500;

UPDATE Funcionario
SET salario = salario * 1.15
WHERE codempresa = 4 AND salario < 2500;

-- 4) Liste todos os nomes distintos dos clientes.

SELECT DISTINCT nome FROM Cliente;

-- 5) Selecione todos os produtos com valor unitário maior que 500.

SELECT * FROM produto
WHERE valorunitario > 500;

-- 6) Mostre todos os Clientes cujo telefone não foi informado (nulo).

SELECT * FROM Cliente
WHERE telefone IS NULL;

-- 7) Mostre todas as vendas do Vendedor Diego Ferreira'

-- 8) Liste os produtos cujo valor esteja entre R$ 100 e R$ 200.

-- 9) Exiba todos os funcionários que pertençam às empresas 2, 4 e 6.

-- 10) Liste o valor e data da Entrega dos Pedidos da cliente 'Carolina Rocha'

-- 11) Selecione todos os clientes cujo nome começa com a letra "A".

-- 12) Liste todos os pedidos feitos em Agosto.

-- 13) Liste todos os funcionários cujo nome termine com a letra "o".

-- 14) Ordene os pedidos do Funcionario Diego Ferreira em ordem decrescente. Exiba somente os pedidos acima de R$ 400

-- 15) Mostre o local a referencia do pedido 417

-- 16) Mostre a descricao de todos os produtos com estoque superior a 530 unidades.

-- 17) Exiba todos os funcionários que possuem salário entre 3000 e 5000.

-- 18) Liste todos os funcionários com salario acima de 3500, ordene por ordem decrescente de salario.

-- 19) Mostre o nome e quantidade dos produtos cujo estoque esteja abaixo de 5, ordene em ordem crescente pelo quantidade

-- 20) Mostre a DESCRIÇÃO e a QUANTIDADE em estoque dos Produtos da empresa 'Casa & Obra' com estoque acima de 40 unidades






