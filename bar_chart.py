from dash import dcc, html, Dash


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


def get_bar_chart_app(dataframe):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_bar_chart(dataframe),
        ],
    )

    app.run_server(debug=True)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_bar_chart_app(dataframe)
