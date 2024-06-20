from dash import Dash, html
from bar_chart import get_bar_chart
from pizza_chart import get_pizza_chart
from scatter_plot import get_scatter_plot
from tree_graph import get_tree_graph

# Começando o processo de criar o dash
app = Dash(__name__)

# Estilização
app.layout = html.Div(
    style={
        "textAlign": "center",
        "fontFamily": "Courier New",
        "display": "flex",
        "flexWrap": "wrap",
        "justifyContent": "center",
    },
    children=[
        html.Div(
            children=[
                html.Div(
                    children="Bar chart:",
                    style={
                        "fontSize": "22px",
                        "color": "#00FFFF",
                    },
                ),
                get_bar_chart(),
            ],
            style={"width": "50%"},
        ),
        html.Div(
            children=[
                html.Div(
                    children="Pie chart:",
                    style={
                        "fontSize": "22px",
                        "color": "#006400",
                    },
                ),
                get_pizza_chart(),
            ],
            style={"width": "50%"},
        ),
        html.Div(
            children=[
                html.Div(
                    children="Tree graph: ",
                    style={
                        "fontSize": "22px",
                        "color": "#FF4500",
                    },
                ),
                get_tree_graph(),
            ],
            style={"width": "50%"},
        ),
        html.Div(
            children=[
                html.Div(
                    children="Scatter plot: ",
                    style={
                        "fontSize": "22px",
                        "color": "#817400",
                    },
                ),
                get_scatter_plot(),
            ],
            style={"width": "50%"},
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
