from dash import dcc

def get_pizza_chart(dataframe) -> dcc.Graph:
    return dcc.Graph(
        id="pie-chart",
        figure={
            "data": [
                {
                    "type": "pie",
                    "name": "Price",
                    "values": dataframe.iloc[:, 3],
                    "labels": dataframe.iloc[:, 0],
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
