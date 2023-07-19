from dash import html
import dash_bootstrap_components as dbc

sidebar_show = [
    dbc.Nav(
        [
            html.Div(
                [
                    dbc.Button(
                        className="bi bi-list 2px btn-sidebar",
                        id="btn-sidebar",
                    ),
                    dbc.Button(
                        children="Dash4Chat",
                        className="btn-title",
                        href="/",
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
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-layout-three-columns",
                        style={"padding": "0vh 1vw"},
                    ),
                    html.Span("Instance"),
                ],
                href="/instance",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(className="bi bi-cpu", style={"padding": "0vh 1vw"}),
                    html.Span("Evaluation"),
                ],
                href="/evaluation",
                active="exact",
                className="side-nav",
            ),
            # dbc.NavLink(
            #     [
            #         html.Span(className="bi bi-columns", style={"padding": "0vh 1vw"}),
            #         html.Span("Visualization"),
            #     ],
            #     href="/visualization",
            #     active="exact",
            #     className="side-nav",
            # ),
        ],
        # card=True,
        vertical=True,
        pills=True,
        style={
            "margin-left": "1vw",
            "align-items": "left",
            "color": "#ffffff",
            # "font-weight": "bold",
            "font-size": "1vw",
            "font-family": "Satoshi, sans-serif",
        },
        className="side-nav",
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
                href="/overview",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-layout-three-columns",
                        style={"padding": "0vh 1vw"},
                    )
                ],
                href="/instance",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-cpu", style={"padding": "0vh 1vw"})],
                href="/evaluation",
                active="exact",
                className="side-nav",
            ),
            # dbc.NavLink(
            #     [html.Span(className="bi bi-columns", style={"padding": "0vh 1vw"})],
            #     href="/qual",
            #     active="exact",
            #     className="side-nav",
            # ),
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
    className="sidebar side-show",
    id="sidebar",
)
