import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from assets import sidebar

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
font_awesome = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
)
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"
external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, font_awesome, icons],
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
        sidebar.sidebar,
        html.Div(
            [
                dbc.Navbar(
                    children=[
                        html.H1(
                            children=["Select Dataset🗃️ →"],
                            style={
                                "margin-left": "3%",
                                "font-weight": "bold",
                                "font-size": "150%",
                            },
                        ),
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        ["DuRecDial2.0 (sample)"],
                                        style={"font-size": 20},
                                    ),
                                    "value": "DuRecDial2.0",
                                },
                                {
                                    "label": html.Span(
                                        ["ReDial (sample)"], style={"font-size": 20}
                                    ),
                                    "value": "ReDial",
                                },
                            ],
                            value="DuRecDial2.0",
                            className="data-selector",
                            optionHeight=50,
                        ),
                    ],
                    className="header",
                    id="header",
                ),
                dash.page_container,
            ],
            id="page_content",
        ),
    ],
    style=layout_style,
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=30005)
