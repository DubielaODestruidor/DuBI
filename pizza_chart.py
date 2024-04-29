from data import get_fruit_df
from dash import dcc

fruit_df = get_fruit_df()


def get_pizza_chart() -> dcc.Graph:
    return dcc.Graph(
        id="pie-chart",
        figure={
            "data": [
                {
                    "values": fruit_df["Price"],
                    "labels": fruit_df["Fruit"],
                    "type": "pie",
                    "name": "Price",
                },
            ],
            "layout": {
                "title": {
                    "text": "Fruit Prices",
                    "font": {"size": 16},
                },
            },
        },
    )
