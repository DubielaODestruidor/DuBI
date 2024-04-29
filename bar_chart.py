from data import get_fruit_df
from dash import dcc

fruit_df = get_fruit_df()


def get_bar_chart() -> dcc.Graph:
    return dcc.Graph(
        id="bar-chart",
        figure={
            "data": [
                {
                    "x": fruit_df["Fruit"],
                    "y": fruit_df["Price"],
                    "type": "bar",
                    "name": "Price",
                    "marker": {
                        "color": fruit_df["Price"],
                        "colorscale": "Rainbow",
                    },
                },
            ],
            "layout": {
                "title": {
                    "text": "Fruit Prices",
                    "font": {"size": 16},
                },
                "xaxis": {
                    "title": {
                        "text": "Fruit",
                        "font": {"size": 15},
                    },
                    "tickfont": {"size": 13},
                },
                "yaxis": {
                    "title": {
                        "text": "Price",
                        "font": {"size": 15},
                    },
                    "tickfont": {"size": 13},
                },
            },
        },
    )
