import pandas as pd
from pandas import DataFrame
from tabulate import tabulate


# Função que cria o DataFrame
def get_fruit_df() -> DataFrame:
    # Dicionário para criar um DataFrame
    fruit_data = {
        "Fruit": [
            "Apple",
            "Banana",
            "Orange",
            "Orange",
            "Grapes",
            "Pinapple",
            "Mango",
            "Kiwi",
            "Strawberry",
        ],
        "Color": [
            "Red",
            "Yellow",
            "Orange",
            "Orange",
            "Green",
            "Yellow",
            "Yellow",
            "Brown",
            "Red",
        ],
        "Taste": [
            "Sweet",
            "Sweet",
            "Sour",
            "Sour",
            "Sweet",
            "Sweet",
            "Sweet",
            "Sour",
            "Sweet",
        ],
        "Quantity": [15, 25, 15, 10, 25, 30, 20, 15, 30],
        "Price": [1.0, 2.0, 3.0, 5.0, 4.0, 5.0, 6.0, 7.0, 8.0],
    }
    # Cria um dataframe a partir do dicionário
    fruit_df = pd.DataFrame(fruit_data)

    # Pega a média dos preços de cada fruta
    mean_price = fruit_df.groupby("Fruit")["Price"].mean()

    # Adiciona a média dos preços no DataFrame
    fruit_df = fruit_df.merge(
        mean_price,
        on="Fruit",
        suffixes=("", "_mean"),
    ).rename(columns={"Price_mean": "Mean Price by Fruit"})

    return fruit_df


# Mostra o DataFrame na linha de comando, quando este arquivo está sendo executado
if __name__ == "__main__":
    print(tabulate(get_fruit_df(), headers="keys", tablefmt="pretty"))
