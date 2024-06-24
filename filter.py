from dash import dcc
from dash.dependencies import Input, Output
from data import get_fruit_df

def create_filter(app) -> dcc.Input:
    @app.callback(
        Output("fruit-table", "data"),
        Input("fruit-table", "filter_query"),
    )
    def update_table(filter):
        fruit_df = get_fruit_df()
        if filter is None:
            return fruit_df.to_dict("records")
        return fruit_df.query(filter).to_dict("records")

    return dcc.Input(
        id="fruit-table",
        type="text",
        placeholder="Filter table",
        style={
            "width": "100%",
            "height": "30px",
            "fontSize": "16px",
            "marginBottom": "10px",
        },
    )
