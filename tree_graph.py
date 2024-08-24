from dash import dcc, html, Dash


def get_tree_graph(dataframe) -> dcc.Graph:
    return dcc.Graph(
        id="tree-graph",
        figure={
            "data": [
                {
                    "type": "treemap",
                    "labels": dataframe["Fruit"],
                    "parents": [""] * len(dataframe),
                    "values": dataframe["Price"],
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
            },
        },
    )


def get_tree_graph_app(dataframe):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_tree_graph(dataframe),
        ],
    )

    app.run_server(debug=True)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_tree_graph_app(dataframe)
