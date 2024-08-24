from dash import Dash, html
from data import get_fruit_df
from bar_chart import get_bar_chart
from pizza_chart import get_pizza_chart
from scatter_plot import get_scatter_plot
from tree_graph import get_tree_graph

# Começando o processo de criar o dash
app = Dash(__name__)
fruit_df = get_fruit_df()

# Estilização
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
    # Filhos do layout
    children=[
        # Gráfico de barras
        html.Div(
            children=[
                html.Div(
                    style={
                        "marginTop": "10px",
                    },
                ),
                get_bar_chart(dataframe=fruit_df),
            ],
            style={
                "width": "40%",
                "marginRight": "10px",
            },
        ),
        # Gráfico de pizza
        html.Div(
            children=[
                html.Div(
                    style={
                        "marginTop": "10px",
                    },
                ),
                get_pizza_chart(dataframe=fruit_df),
            ],
            style={
                "width": "40%",
                "marginLeft": "10px",
            },
        ),
        # Gráfico de árvore
        html.Div(
            children=[
                html.Div(
                    style={
                        "marginTop": "20px",
                    },
                ),
                get_tree_graph(dataframe=fruit_df),
            ],
            style={
                "width": "40%",
                "marginRight": "10px",
            },
        ),
        # Gráfico de dispersão
        html.Div(
            children=[
                html.Div(
                    style={
                        "marginTop": "20px",
                    },
                ),
                get_scatter_plot(dataframe=fruit_df),
            ],
            style={
                "width": "40%",
                "marginLeft": "10px",
            },
        ),
    ],
)

# Rodando o Dash
if __name__ == "__main__":
    app.run_server(debug=True)
