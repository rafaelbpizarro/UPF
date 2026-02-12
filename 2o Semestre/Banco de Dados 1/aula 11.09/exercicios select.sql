---Exercicios de função de agregação, having, select com join

-- 1. Liste a quantidade total de funcionários em cada empresa

select * from empresa

SELECT codempresa, COUNT(*) AS total_funcionarios
FROM funcionario
GROUP BY codempresa

SELECT e.razaosocial as empresa, COUNT(f.nome) AS total_funcionarios
FROM funcionario f
JOIN empresa e ON f.codempresa = e.id
GROUP BY e.id
--HAVING COUNT(f.nome)>5          QUANDO A QUANTIDADE DE FUNCIONARIOS FOR MAIOR QUE 5

-- 2. Liste o número de produtos cadastrados por empresa

SELECT codempresa, COUNT(*) AS total_produtos
FROM produto
GROUP BY codempresa
ORDER BY codempresa;

-- 3. Mostre a quantidade de clientes cadastrados sem telefone informado 

SELECT COUNT(*) AS sem_telefone	
FROM cliente
WHERE telefone IS NULL;

-- 4.Calcule a soma total de todos os estoques de produtos.


-- 5.Mostre o menor valor de pedido registrado.


-- 6. Mostre a média do valor total dos pedidos.



-- 7. Calcule a média do valor total dos pedidos feitos em 2025

-- 8. -- Mostre o código da empresa e o preço médio dos produtos, exibindo apenas empresas com preço médio superior a 100.


-- 9.  Liste o código do cliente e o total gasto em pedidos,mostrando apenas clientes cujo total gasto seja maior que 1000.


--10. -- exibindo apenas empresas com mais de 3 produtos.


--11. Encontrar o valor do pedido mais caro registrado por cada funcionário.

	
	
--12.Usando LEFT JOIN, liste o código do pedido, o nome do cliente e o valor total.


--13  Crie uma view chamada vw_pedidos_funcionarios que mostre:
--- o código do pedido
--- o nome do funcionário que atendeu
--- o valor total do pedido




-- 14. -- Liste o código do cliente e o total gasto em pedidos,
-- mostrando apenas clientes que tenham realizado pelo menos 2 pedidos.



---15.-- Mostre o código da empresa e a média de preços dos produtos,
-- mas exiba apenas empresas cuja média de preços esteja entre 50 e 200.