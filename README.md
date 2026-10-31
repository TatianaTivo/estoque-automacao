# Automação de Estoque em Python

Programa que lê uma planilha de estoque e gera um relatório de compras com os produtos que estão no mínimo ou abaixo dele.

## Como funciona

1. Lê o arquivo `estoque.csv` (produto, quantidade, mínimo e ideal).
2. Filtra os produtos com quantidade menor ou igual ao mínimo.
3. Calcula quanto comprar para chegar ao estoque ideal.
4. Salva o resultado em `relatorio_compras.csv`.

## Como rodar

1. Instale o Python 3 e o pandas: `python -m pip install pandas`
2. Rode: `python estoque.py`

## Por que fiz este projeto

Trabalhei durante 4 anos com controle de estoque e compras e após passar por algumas dificuldades de perto, quis automatizar uma tarefa que fazia manualmente em planilhas.