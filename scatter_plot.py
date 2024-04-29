from data import get_fruit_df
from dash import dcc

fruit_df = get_fruit_df()


def get_scatter_plot() -> dcc.Graph:
    return dcc.Graph(
        id="scatter-plot",
        figure={
            "data": [
                {
                    "x": fruit_df["Quantity"],
                    "y": fruit_df["Price"],
                    "type": "scatter",
                    "mode": "markers",
                    "name": "Price",
                    "marker": {
                        "color": fruit_df["Price"],
                        "colorscale": "Viridis",
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
                        "text": "Quantity",
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
