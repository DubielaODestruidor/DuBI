import webbrowser

from dash import Dash, dcc, html


def get_pizza_chart(data) -> dcc.Graph:
    return dcc.Graph(
        id="pie-chart",
        figure={
            "data": [
                {
                    "type": "pie",
                    "name": "Price",
                    "values": data.iloc[:, 3],
                    "labels": data.iloc[:, 0],
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


def get_pizza_chart_app(data):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_pizza_chart(data),
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
    get_pizza_chart_app(dataframe)
