from dash import dcc, html, Dash


def get_scatter_plot(dataframe) -> dcc.Graph:
    return dcc.Graph(
        id="scatter-plot",
        figure={
            "data": [
                {
                    "type": "scatter",
                    "mode": "markers",
                    "name": "Price",
                    "x": dataframe["Quantity"],
                    "y": dataframe["Price"],
                    "marker": {
                        "color": dataframe["Price"],
                        "colorscale": "Viridis",
                    },
                },
            ],
            "layout": {
                "title": {
                    "text": "Fruit Prices by Quantity",
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


def get_scatter_plot_app(dataframe):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_scatter_plot(dataframe),
        ],
    )

    app.run_server(debug=True)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_scatter_plot_app(dataframe)
