from dash import dcc, html, Dash
import webbrowser


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
                    "text": dataframe["Fruit"],
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
        style={
            "width": "100vw",
            "height": "100vh",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
        },
    )

    url = "http://127.0.0.1:8050/"
    webbrowser.open(url)
    app.run_server(debug=True, use_reloader=False)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_scatter_plot_app(dataframe)
