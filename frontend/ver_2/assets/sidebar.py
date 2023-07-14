from dash import html
import dash_bootstrap_components as dbc
from assets import css

sidebar_show = [
    dbc.Nav(
        [
            html.Div(
                [
                    dbc.Button(
                        className="bi bi-list 2px",
                        style={
                            "height": "7vh",
                            "margin-left": "0.5vw",
                            "font-size": "1.5vw",
                            # "font-weight": "bold",
                            "font-family": "Satoshi, sans-serif",
                            "align-items": "center",
                            "display": "flex",
                            "background-color": "transparent",
                            "border": "transparent",
                            "color": "#e4e3fa",
                        },
                        id="btn-sidebar",
                    ),
                    dbc.Button(
                        children="Dash4Chat",
                        style={
                            "background-color": "transparent",
                            "border": "transparent",
                            "color": "#e4e3fa",
                            "font-size": "1.5vw",
                            # "font-weight": "bold",
                            "font-family": "Satoshi, sans-serif",
                            "margin-left": "1vw",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                },
                id="header-side-box",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("Overview"),
                ],
                href="/overview",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(className="bi bi-columns", style={"padding": "0vh 1vw"}),
                    html.Span("Conversation"),
                ],
                href="/conversation",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-bar-chart", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("User"),
                ],
                href="/user",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-card-text", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("Qualitative"),
                ],
                href="/qualitative",
                active="exact",
                style=css.NAVSTYLE,
            ),
        ],
        # card=True,
        vertical=True,
        pills=False,
        style={
            "margin-left": "2vw",
            "align-items": "left",
            "color": "#ffffff",
            # "font-weight": "bold",
            "font-size": "1vw",
            "font-family": "Satoshi, sans-serif",
        },
    ),
]

sidebar_hidden = [
    dbc.Nav(
        [
            dbc.Button(
                className="bi bi-list 2px",
                style={
                    "height": "7vh",
                    "margin-left": "0.5vw",
                    "font-size": "1.5vw",
                    # "font-weight": "bold",
                    "font-family": "Satoshi, sans-serif",
                    "align-items": "center",
                    "display": "flex",
                    "background-color": "transparent",
                    "border": "transparent",
                    "color": "#e4e3fa",
                },
                id="btn-sidebar",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-house-door", style={"padding": "0vh 1vw"})],
                href="/",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-columns", style={"padding": "0vh 1vw"})],
                href="/description",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-bar-chart", style={"padding": "0vh 1vw"})],
                href="/qual-viz",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-card-text", style={"padding": "0vh 1vw"})],
                href="/quan-viz",
                active="exact",
                style=css.NAVSTYLE,
            ),
        ],
        # card=True,
        vertical=True,
        pills=False,
        style={
            "align-items": "left",
            "color": "#aeaeec",
            "font-weight": "bold",
            "font-size": "1vw",
        },
    ),
]

sidebar = html.Div(
    children=sidebar_show,
    style=css.SIDEBAR_SHOW,
    id="sidebar",
)
