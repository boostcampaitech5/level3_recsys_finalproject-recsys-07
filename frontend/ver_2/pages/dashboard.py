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
    'width': '85vw',
    "padding": "2vh 1vw",
    "display": 'flex',
}

FIGURE_BLANK = {
    'width': '23vw',
    'height': '20vh',
    'padding':'2vh 2vw',
    'background-color': '#ffffff',
    'font-weight':'bold',
    'margin': '1vh 1vw',
}
content = html.Div(
    [
        html.Div([
            'figure-1'
        ],
        style=FIGURE_BLANK),
        html.Div([
            'figure-2'
        ],
        style=FIGURE_BLANK),
        html.Div([
            'figure-3'
        ],
        style=FIGURE_BLANK),
    ],
    style=CONTENT_STYLE,
    id='page-content',
)

layout_style = {
    # 'display': 'flex'
    'background-color':'#f2f5fa',
    'height': '93vh',
}

layout = html.Div([
    # dcc.Location(id="url"),
    content,
    ],
    style=layout_style,
)