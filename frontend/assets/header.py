import dash_bootstrap_components as dbc
from dash import dcc, html

header = (
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
                [
                    {
                        "label": html.Span(
                            ["DuRecDial2.0 (sample)"],
                            style={"font-size": 20},
                        ),
                        "value": "DuRecDial2.0",
                    },
                    {
                        "label": html.Span(
                            ["ReDial (sample)"], style={"font-size": 20}
                        ),
                        "value": "ReDial",
                    },
                ],
                value="DuRecDial2.0",
                className="data-selector",
                optionHeight=50,
            ),
        ],
        className="header",
        id="header",
    ),
)
