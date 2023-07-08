import os
import dash
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table, callback, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate
dash.register_page(__name__, path='/')

# the style arguments for the sidebar. We use position:fixed and a fixed width

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "display": 'flex',
}


content = html.Div(
    [

        html.H1('Multi-page app with Dash Pages'),
        
        html.Div([
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]),
    ]
)

layout_style = {
    # 'display': 'flex'
    'background-color':'#e6e7e9',
    'height': '95vh',
}

layout = html.Div([
    # dcc.Location(id="url"),
    content,
    ],
    style=layout_style,
)