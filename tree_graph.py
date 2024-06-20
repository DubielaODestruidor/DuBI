from data import get_fruit_df
from dash import dcc

fruit_df = get_fruit_df()


def get_tree_graph() -> dcc.Graph:
    return dcc.Graph(
        id="tree-graph",
        figure={
            "data": [
                {
                    "type": "treemap",
                    "labels": fruit_df["Fruit"],
                    "parents": [""] * len(fruit_df),
                    "values": fruit_df["Price"],
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
            },
        },
    )
