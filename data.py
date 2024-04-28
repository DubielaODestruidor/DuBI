import pandas as pd
from tabulate import tabulate

# Dicionário para criar um dataframe
fruit_data = {
    "fruit": ["Apple", "Banana", "Orange", "Grapes", "Apple", "Banana"],
    "Color": ["Red", "Yellow", "Orange", "Purple", "Red", "Yellow"],
    "Taste": ["Sweet", "Sweet", "Bittersweet", "Sweet", "Bittersweet", "Sweet"],
    "Price": [0.5, 0.25, 0.35, 0.75, 0.6, 0.3],
}
# Cria um dataframe a partir do dicionário
fruit_df = pd.DataFrame(fruit_data)

# Pega a média dos preços de cada fruta
mean_price = fruit_df.groupby("fruit")["Price"].mean()

# Adiciona a média dos preços no dataframe
fruit_df = fruit_df.merge(
    mean_price,
    on="fruit",
    suffixes=("", "_mean"),
).rename(columns={"Price_mean": "Mean Price by Fruit"})

# Mostra o dataframe na linha de comando
# print(tabulate(fruit_df, headers="keys", tablefmt="fancy_grid"))
