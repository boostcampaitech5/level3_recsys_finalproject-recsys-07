import dash
from dash import Dash, Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
from assets import css

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
font_awsome = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
)
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, font_awsome, icons],
    use_pages=True,
    suppress_callback_exceptions=True,
)
sidebar_show = [
    dbc.Nav(
        [
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("Home"),
                ],
                href="/",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(className="bi bi-columns", style={"padding": "0vh 1vw"}),
                    html.Span("Description"),
                ],
                href="/description",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-bar-chart", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("qual-viz"),
                ],
                href="/qual-viz",
                active="exact",
                style=css.NAVSTYLE,
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-card-text", style={"padding": "0vh 1vw"}
                    ),
                    html.Span("quan-viz"),
                ],
                href="/quan-viz",
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
            "color": "#aeaeec",
            "font-weight": "bold",
            "font-size": "1vw",
        },
    ),
]

sidebar_hidden = [
    dbc.Nav(
        [
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
    style=css.SIDEBAR_STYLE,
    id="sidebar",
)


navbar = dbc.Navbar(
    children=[
        html.Div(
            [
                dbc.Button(
                    className="bi bi-list 2px",
                    style={
                        "height": "7vh",
                        "margin-left": "0.5vw",
                        "font-size": "1.5vw",
                        "font-weight": "bold",
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
                        "font-weight": "bold",
                        "margin-left": "1vw",
                    },
                ),
            ],
            style=css.HEADER_BOX_SHOW,
            id="header-side-box",
        )
    ],
    # brand="Dash4Chat",
    # brand_href="",
    color="#6690ff",
    # dark=True,
    # fluid=True,
    style=css.HEADER_STYLE,
)
layout_style = {
    "display": "horizontal",
}
app.layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Location(id="url"),
        navbar,
        html.Span(
            [
                sidebar,
                dash.page_container,
            ],
            style={
                "display": "flex",
                "min-width": "100%",
            },
        ),
    ],
    style=layout_style,
)


@app.callback(
    [
        Output("header-side-box", "style"),
        Output("sidebar", "style"),
        Output("sidebar", "children"),
        Output("_pages_content", "style"),
        Output("side_click", "data"),
    ],
    [Input("btn-sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ],
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            header_sb_style = css.HEADER_BOX_HIDDEN
            sidebar_style = css.SIDEBAR_HIDDEN
            sidebar_children = sidebar_hidden
            content_style = css.CONTENT_SIDE_OFF
            cur_nclick = "HIDDEN"
        else:
            header_sb_style = css.HEADER_BOX_SHOW
            sidebar_style = css.SIDEBAR_STYLE
            sidebar_children = sidebar_show
            content_style = css.CONTENT_SIDE_ON
            cur_nclick = "SHOW"
    else:
        header_sb_style = css.HEADER_BOX_SHOW
        sidebar_style = css.SIDEBAR_STYLE
        sidebar_children = sidebar_show
        content_style = css.CONTENT_SIDE_ON
        cur_nclick = "SHOW"

    return header_sb_style, sidebar_style, sidebar_children, content_style, cur_nclick


if __name__ == "__main__":
    app.run_server(debug=True, port=30002)
