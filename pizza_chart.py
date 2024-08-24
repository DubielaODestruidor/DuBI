from dash import dcc, html, Dash


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


def get_pizza_chart_app(dataframe):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_pizza_chart(dataframe),
        ],
    )

    app.run_server(debug=True)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_pizza_chart_app(dataframe)
