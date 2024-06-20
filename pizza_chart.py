from data import get_fruit_df
from dash import dcc

fruit_df = get_fruit_df()


def get_pizza_chart() -> dcc.Graph:
    return dcc.Graph(
        id="pie-chart",
        figure={
            "data": [
                {
                    "type": "pie",
                    "name": "Price",
                    "values": fruit_df["Price"],
                    "labels": fruit_df["Fruit"],
                },
            ],
            "layout": {
                "title": {
                    "text": "Fruit Percentage",
                    "font": {"size": 16},
                },
            },
        },
    )
