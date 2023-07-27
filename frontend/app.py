import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from assets import sidebar, header


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
pretendard = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/static/pretendard.css"
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"
external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, pretendard, icons],
    external_scripts=external_script,
    use_pages=True,
    suppress_callback_exceptions=True,
)
app.scripts.config.serve_locally = True

layout_style = {
    "display": "horizontal",
}
app.layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Location(id="url"),
        # TODO: 데이터 전처리과정 비동기처리하기.
        sidebar.sidebar,
        html.Div(
            [
                header.header,
                dash.page_container,
            ],
            id="page_content",
        ),
    ],
    style=layout_style,
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=30005)
