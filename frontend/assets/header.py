from dash import dcc, html, callback, Input, Output, State
import dash
import dash_bootstrap_components as dbc

header = html.Div(
    [
        dbc.Navbar(
            children=[
                html.H1(
                    children=["Select Dataset🗃️ →"],
                    style={
                        "margin-left": "3%",
                        "font-weight": "bold",
                        "font-size": "150%",
                    },
                ),
                dcc.Dropdown(
                    id="header-data-dropdown",
                    value="",
                    className="data-selector",
                    optionHeight=50,
                ),
            ],
            className="header",
            id="header",
        )
    ]
)


@callback(
    Output("header-data-dropdown", "options"),
    Input("filename-store", "modified_timestamp"),
    State("filename-store", "data"),
)
def get_filename(ts, filename):
    if ts is None:
        raise dash.exceptions.PreventUpdate
    return [{"label": filename, "value": filename}]
