from dash import Dash, html
from bar_chart import get_bar_chart
from pizza_chart import get_pizza_chart
from scatter_plot import get_scatter_plot
from tree_graph import get_tree_graph
import webbrowser


def get_dashboard_app(data):
    app = Dash(__name__)

    app.layout = html.Div(
        style={
            "textAlign": "center",
            "fontFamily": "Courier New",
            "display": "flex",
            "flexWrap": "wrap",
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor": "#f0f0f0",
            "padding": "10px",
            "height": "100%",
            "width": "100%",
        },
        children=[
            html.Div(
                children=[
                    html.Div(
                        style={
                            "marginTop": "10px",
                        },
                    ),
                    get_bar_chart(data=data),
                ],
                style={
                    "width": "40%",
                    "marginRight": "10px",
                },
            ),
            html.Div(
                children=[
                    html.Div(
                        style={
                            "marginTop": "10px",
                        },
                    ),
                    get_pizza_chart(data=data),
                ],
                style={
                    "width": "40%",
                    "marginLeft": "10px",
                },
            ),
            html.Div(
                children=[
                    html.Div(
                        style={
                            "marginTop": "20px",
                        },
                    ),
                    get_tree_graph(data=data),
                ],
                style={
                    "width": "40%",
                    "marginRight": "10px",
                },
            ),
            html.Div(
                children=[
                    html.Div(
                        style={
                            "marginTop": "20px",
                        },
                    ),
                    get_scatter_plot(data=data),
                ],
                style={
                    "width": "40%",
                    "marginLeft": "10px",
                },
            ),
        ],
    )

    url = "http://127.0.0.1:8050/"
    webbrowser.open(url)
    app.run_server(debug=True, use_reloader=False)


if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_dashboard_app(dataframe)
