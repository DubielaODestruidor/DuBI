from dash import dcc, html, Dash
import webbrowser


def get_tree_graph(data) -> dcc.Graph:
    return dcc.Graph(
        id="tree-graph",
        figure={
            "data": [
                {
                    "type": "treemap",
                    "labels": data["Fruit"],
                    "parents": [""] * len(data),
                    "values": data["Price"],
                    "marker": {
                        "color": data["Price"],
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


def get_tree_graph_app(data):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_tree_graph(data),
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
    get_tree_graph_app(dataframe)
