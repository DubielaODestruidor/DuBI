import webbrowser

from dash import Dash, dcc, html


def get_bar_chart(data) -> dcc.Graph:
    return dcc.Graph(
        id="bar-chart",
        figure={
            "data": [
                {
                    # Define o tipo de gráfico e suas propriedades
                    "type": "bar",
                    "name": "Price",
                    "x": data["Fruit"],
                    "y": data["Price"],
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


# Função que cria um aplicativo Dash com o gráfico de barras
def get_bar_chart_app(data):
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            get_bar_chart(data),
        ],
        style={
            "width": "100vw",
            "height": "100vh",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
        },
    )

    # Abre o navegador com o aplicativo, na porta padrão usado pelo Dash
    url = "http://127.0.0.1:8050/"
    webbrowser.open(url)
    app.run_server(debug=True, use_reloader=False)


# Executa o aplicativo quando script é chamado como principal
if __name__ == "__main__":
    from data import get_fruit_df

    dataframe = get_fruit_df()
    get_bar_chart_app(dataframe)
