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
                        children="DASHMON",
                        className="btn-title",
                        href="/",
                    ),
                ],
                id="header-side-box",
                className="side-header",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door side-nav-icon",
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
                        className="bi bi-layout-three-columns side-nav-icon",
                    ),
                    html.Span("Instance"),
                ],
                href="/instance",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-columns side-nav-icon",
                    ),
                    html.Span("Data Analysis"),
                ],
                href="/dataanalysis",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-cpu side-nav-icon",
                    ),
                    html.Span("Model Evaluation"),
                ],
                href="/modelevaluation",
                active="exact",
                className="side-nav",
            ),
        ],
        vertical=True,
        pills=True,
    ),
]

sidebar_hidden = [
    dbc.Nav(
        [
            dbc.Button(
                className="bi bi-list 2px btn-sidebar",
                id="btn-sidebar",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door side-nav-icon",
                    )
                ],
                href="/overview",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-layout-three-columns side-nav-icon",
                    )
                ],
                href="/instance",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-columns side-nav-icon")],
                href="/dataanalysis",
                active="exact",
                className="side-nav",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-cpu side-nav-icon")],
                href="/modelevaluation",
                active="exact",
                className="side-nav",
            ),
        ],
        vertical=True,
        pills=False,
    ),
]

sidebar = html.Div(
    children=sidebar_show,
    className="sidebar side-show",
    id="sidebar",
)
