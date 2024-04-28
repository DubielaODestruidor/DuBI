from data import fruit_df
from dash import Dash, dcc, html

# Começando o processo de criar o dash
app = Dash(__name__)

# Estilização
app.layout = html.Div(
    style={
        "width": "1200px",
        "height": "100vh",
        "margin": "auto",
        "textAlign": "center",
        "fontFamily": "Courier New",
    },
    children=[
        html.Div(
            children="Bar chart:",
            style={"fontSize": "22px"},
        ),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {
                        "x": fruit_df["fruit"],
                        "y": fruit_df["Price"],
                        "type": "bar",
                        "name": "Price",
                        "marker": {
                            "color": fruit_df["Price"],
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
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
