import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        html.H1(children="This is our Analytics page"),
        html.Div(["introduction page"]),
    ]
)
