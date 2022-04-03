---------------------------------------------------------VARIAVEIS--------------------------------------------------------

DECLARE @PERIODO_ATUAL INT
DECLARE @PERIODO_ANTERIOR INT
--PREMISSA DOS ULTIMOS 3 MESES DO CLIENTE
SET @PERIODO_ATUAL = cast(concat(str(year(max(getdate()))),str(month(max(getdate())))) as integer)
SET @PERIODO_ANTERIOR = cast(concat(str(year(max(DATEADD(MONTH,-3,getdate())))),str(month(max(DATEADD(MONTH,-3,getdate()))))) as integer);
-------------------------------------------------------------TB_CLIENTE---------------------------------------------------
WITH TB_CLIENTE AS
(SELECT 
      cliente_id
      ,CASE 
           WHEN cpf IS NOT NULL THEN (REPLICATE('0', 14 - LEN(cpf)) + RTrim(cpf))
           ELSE (REPLICATE('0', 14 - LEN(cnpj)) + RTrim(cnpj))
      END cpf_cnpj
      ,CASE 
           WHEN cpf IS NOT NULL THEN nome_civil
           ELSE nome_razaosocial
      END nome_cliente
      ,CASE 
           WHEN cpf IS NOT NULL THEN nome_social
           ELSE nome_marca
      END nome_social
      ,CASE 
           WHEN cpf IS NOT NULL THEN estado_civil
           ELSE 'N/A'
      END estado_civil
      ,CASE 
           WHEN cpf IS NOT NULL THEN sexo
           ELSE 'N/A'
      END sexo
      ,nacionalidade
      ,data_nascimento
FROM [dbo].[catalog_clientepessoanatural]
),

-------------------------------------------------------------TB_RENDA_FIXA---------------------------------------------------
TB_RENDA_FIXA AS 
(SELECT
      cliente_id
      ,max(CAST(CONCAT(STR(YEAR(data_renda)),(REPLICATE('0', 2 - LEN(MONTH(data_renda))) + RTrim(MONTH(data_renda)))) AS INTEGER)) AS periodo
      ,SUM(CAST(REPLACE(renda_fixa,',','.') AS FLOAT))/count(distinct(CAST(CONCAT(STR(YEAR(data_renda)),(REPLICATE('0', 2 - LEN(MONTH(data_renda))) + RTrim(MONTH(data_renda)))) AS INTEGER))) as entrada
      ,NULL AS saida
 FROM [dbo].[catalog_valorcliente]
 WHERE (CAST(CONCAT(STR(YEAR(data_renda)),(REPLICATE('0', 2 - LEN(MONTH(data_renda))) + RTrim(MONTH(data_renda)))) AS INTEGER)) between  @PERIODO_ANTERIOR and @PERIODO_ATUAL
 GROUP BY 
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_renda)),(REPLICATE('0', 2 - LEN(MONTH(data_renda))) + RTrim(MONTH(data_renda)))) AS INTEGER)
),

-------------------------------------------------------------TB_CARTAO_CREDITO---------------------------------------------------
TB_CARTAO_CREDITO AS 
(SELECT
      cliente_id
      ,max(CAST(CONCAT(STR(YEAR(data_creditcard)),(REPLICATE('0', 2 - LEN(MONTH(data_creditcard))) + RTrim(MONTH(data_creditcard)))) AS INTEGER)) AS periodo
      ,NULL AS entrada
      ,SUM(CAST(REPLACE(creditcard_valorfaturapg,',','.') AS FLOAT))/count(distinct(CAST(CONCAT(STR(YEAR(data_creditcard)),(REPLICATE('0', 2 - LEN(MONTH(data_creditcard))) + RTrim(MONTH(data_creditcard)))) AS INTEGER))) as saida
 FROM [dbo].[catalog_valorcliente]
 WHERE (CAST(CONCAT(STR(YEAR(data_creditcard)),(REPLICATE('0', 2 - LEN(MONTH(data_creditcard))) + RTrim(MONTH(data_creditcard)))) AS INTEGER)) between  @PERIODO_ANTERIOR and @PERIODO_ATUAL
 GROUP BY 
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_creditcard)),(REPLICATE('0', 2 - LEN(MONTH(data_creditcard))) + RTrim(MONTH(data_creditcard)))) AS INTEGER)
),

-------------------------------------------------------------TB_CONTACORRENTE---------------------------------------------------
TB_CONTACORRENTE AS 
(SELECT
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_contacorrente)),(REPLICATE('0', 2 - LEN(MONTH(data_contacorrente))) + RTrim(MONTH(data_contacorrente)))) AS INTEGER) AS periodo
      ,SUM(CAST(REPLACE(contacorrente,',','.') AS FLOAT)) AS entrada
      ,NULL AS saida
 FROM [dbo].[catalog_valorcliente] 
 GROUP BY 
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_contacorrente)),(REPLICATE('0', 2 - LEN(MONTH(data_contacorrente))) + RTrim(MONTH(data_contacorrente)))) AS INTEGER)
),

-------------------------------------------------------------TB_CONTAPOUPANCA---------------------------------------------------
TB_CONTAPOUPANCA AS 
(SELECT
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_contapoupanca)),(REPLICATE('0', 2 - LEN(MONTH(data_contapoupanca))) + RTrim(MONTH(data_contapoupanca)))) AS INTEGER) AS periodo
      ,SUM(CAST(REPLACE(contapoupanca,',','.') AS FLOAT)) AS entrada
      ,NULL AS saida
 FROM [dbo].[catalog_valorcliente]
 --WHERE data_contapoupanca = 
 GROUP BY 
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_contapoupanca)),(REPLICATE('0', 2 - LEN(MONTH(data_contapoupanca))) + RTrim(MONTH(data_contapoupanca)))) AS INTEGER)
),

-------------------------------------------------------------TB_PATRIMONIOS---------------------------------------------------
TB_PATRIMONIOS AS 
(SELECT
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_patrimonios)),(REPLICATE('0', 2 - LEN(MONTH(data_patrimonios))) + RTrim(MONTH(data_patrimonios)))) AS INTEGER) AS periodo
      ,SUM(CAST(REPLACE(patrimonios,',','.') AS FLOAT)) AS entrada
      ,NULL AS saida
      
 FROM [dbo].[catalog_valorcliente]
 GROUP BY 
      cliente_id
      ,CAST(CONCAT(STR(YEAR(data_patrimonios)),(REPLICATE('0', 2 - LEN(MONTH(data_patrimonios))) + RTrim(MONTH(data_patrimonios)))) AS INTEGER)
),

-------------------------------------------------------------TB_CONSOLIDADO_FINANC_EMPRESTIMO---------------------------------------------------
TB_CONSOLIDADO_FINANC_EMPRESTIMO AS
(SELECT 
       CASE WHEN A.cliente_id IS NOT NULL THEN A.cliente_id ELSE B.cliente_id END cliente_id
       ,NULL AS entrada
       ,(SUM(CAST(REPLACE(B.valor_parcela_financiamento,',','.') AS FLOAT))+SUM(CAST(REPLACE(A.valor_parcela_emprestimo,',','.') AS FLOAT))) AS saida
       FROM (SELECT
                   cliente_id
                   ,valor_emprestimo
                   ,valor_parcela_emprestimo
                   ,data_inicio_emprest_contrato
                   ,data_fim_emprest_contrato
                   ,CASE 
                        WHEN DATEDIFF(DAY, data_fim_emprest_contrato,GETDATE())> 0 THEN 'ATIVO' 
                        ELSE 'INATIVO' 
                   END status_emprestimo
            FROM [dbo].[catalog_valorcliente]) A 
       FULL OUTER JOIN (SELECT
                              cliente_id
                              ,valor_financiamento
                              ,valor_parcela_financiamento
                              ,data_inicio_financ_contrato
                              ,data_fim_financ_contrato
                              ,CASE 
                                    WHEN DATEDIFF(DAY, data_fim_financ_contrato,GETDATE())> 0 THEN 'ATIVO' 
                                    ELSE 'INATIVO' 
                               END status_financiamento
            FROM [dbo].[catalog_valorcliente]) B 
                ON A.cliente_id = B.cliente_id
                AND A.status_emprestimo = 'ATIVO'
                AND B.status_financiamento = 'ATIVO'
				GROUP BY CASE WHEN A.cliente_id IS NOT NULL THEN A.cliente_id ELSE B.cliente_id END),
TB_CONSOLIDADO_TOTAL AS (
      --SELECT * FROM TB_CLIENTE
      --UNION
      SELECT * FROM TB_RENDA_FIXA
      UNION
      SELECT * FROM TB_CARTAO_CREDITO
      UNION
      SELECT * FROM TB_CONTACORRENTE
      UNION
      SELECT * FROM TB_CONTAPOUPANCA
      UNION
      SELECT * FROM TB_PATRIMONIOS
      UNION
      SELECT * FROM TB_CONSOLIDADO_FINANC_EMPRESTIMO
)
SELECT * FROM TB_CONSOLIDADO_TOTAL