import dash
from dash import html, dcc

dash.register_page(__name__)

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
            'figure-10'
        ],
        style=FIGURE_BLANK),
        html.Div([
            'figure-11'
        ],
        style=FIGURE_BLANK),
        html.Div([
            'figure-12'
        ],
        style=FIGURE_BLANK),
    ],
    style=CONTENT_STYLE
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