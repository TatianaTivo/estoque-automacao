import sys
import pandas as pd

ARQUIVO = "estoque.csv"
COLUNAS = ["produto", "quantidade", "minimo", "ideal"]

try:
    estoque = pd.read_csv(ARQUIVO)
except FileNotFoundError:
    print(f"Erro: não encontrei o arquivo {ARQUIVO}.")
    sys.exit(1)

for coluna in COLUNAS:
    if coluna not in estoque.columns:
        print(f"Erro: falta a coluna '{coluna}' no arquivo.")
        sys.exit(1)

abaixo = estoque[estoque["quantidade"] <= estoque["minimo"]].copy()
abaixo["comprar"] = abaixo["ideal"] - abaixo["quantidade"]

print("Produtos abaixo do mínimo:")
print(abaixo)

abaixo.to_csv("relatorio_compras.csv", index=False)
abaixo.to_excel("relatorio_compras.xlsx", index=False)