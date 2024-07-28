from dash import dcc

def get_bar_chart(dataframe) -> dcc.Graph:
    return dcc.Graph(
        id="bar-chart",
        figure={
            "data": [
                {
                    "type": "bar",
                    "name": "Price",
                    "x": dataframe["Fruit"],
                    "y": dataframe["Price"],
                    "marker": {
                        "color": dataframe["Price"],
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
