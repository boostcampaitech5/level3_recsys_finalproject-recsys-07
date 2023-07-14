import dash
from dash import Dash, Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
from assets import sidebar

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
font_awsome = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
)
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"
external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, font_awsome, icons],
    external_scripts=external_script,
    use_pages=True,
    suppress_callback_exceptions=True,
)
app.scripts.config.serve_locally = True


navbar = dbc.Navbar(
    children=[],
    # brand="Dash4Chat",
    # brand_href="",
    # color="#6690ff",
    # dark=True,
    # fluid=True,
    className="header",
)
layout_style = {
    "display": "horizontal",
}
app.layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Location(id="url"),
        sidebar.sidebar,
        html.Div(
            [
                navbar,
                dash.page_container,
            ],
            id="page_content",
            className="sidebar side-show",
        ),
    ],
    style=layout_style,
)


@app.callback(
    [
        Output("sidebar", "className"),
        Output("sidebar", "children"),
        Output("page_content", "className"),
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
            sidebar_className = "sidebar side-hidden"
            sidebar_children = sidebar.sidebar_hidden
            content_className = "content content-side-hidden"
            cur_nclick = "HIDDEN"
        else:
            sidebar_className = "sidebar side-show"
            sidebar_children = sidebar.sidebar_show
            content_className = "content content-side-show"
            cur_nclick = "SHOW"
    else:
        sidebar_className = "sidebar side-show"
        sidebar_children = sidebar.sidebar_show
        content_className = "content content-side-show"
        cur_nclick = "SHOW"

    return sidebar_className, sidebar_children, content_className, cur_nclick


if __name__ == "__main__":
    app.run_server(debug=True, port=30002)
