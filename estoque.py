import pandas as pd

estoque = pd.read_csv("estoque.csv")

abaixo = estoque[estoque["quantidade"] <= estoque["minimo"]].copy()
abaixo["comprar"] = abaixo["ideal"] - abaixo["quantidade"]

print("Produtos abaixo do mínimo:")
print(abaixo)

abaixo.to_csv("relatorio_compras.csv", index=False)