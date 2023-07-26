from dash import Input, Output, State, callback, dcc, html
import dash
import dash_bootstrap_components as dbc
import io
import pandas as pd

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
            html.H1(
                children=["Upload Dataset🗃️"],
                # style={"margin-left": "10%", "margin-bottom": "5%"},
                className="side-nav",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-info-circle side-nav-icon",
                    ),
                    html.Span("README"),
                ],
                href="/readme",
                active="exact",
                className="side-nav",
            ),
            dcc.Upload(
                id="upload-data",
                children=html.Div([html.A("Drag & Drop or Select File")]),
                style={
                    "width": "70%",
                    "height": "50%",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "5% 3% 3% 10%",
                    "font-size": "15px",
                },
            ),
            dcc.Store(
                id="filename-store",
            ),
            dcc.Store(
                id="date-store",
            ),
            dcc.Store(
                id="data-store",
            ),
            html.Ul(id="file-list"),
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


@callback(
    [
        Output("header", "className"),
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
            header_className = "header content-side-hidden"
            sidebar_className = "sidebar side-hidden"
            sidebar_children = sidebar_hidden
            content_className = "content content-side-hidden"
            cur_nclick = "HIDDEN"
        else:
            header_className = "header content-side-show"
            sidebar_className = "sidebar side-show"
            sidebar_children = sidebar_show
            content_className = "content content-side-show"
            cur_nclick = "SHOW"
    else:
        header_className = "header content-side-show"
        sidebar_className = "sidebar side-show"
        sidebar_children = sidebar_show
        content_className = "content content-side-show"
        cur_nclick = "SHOW"

    return (
        header_className,
        sidebar_className,
        sidebar_children,
        content_className,
        cur_nclick,
    )


@callback(
    Output("filename-store", "data"),
    Output("date-store", "data"),
    Output("data-store", "data"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def store_output(content_string, filename, date):
    if content_string is not None:
        print("uploaded file: ", filename)
        try:
            if "csv" in filename:
                df = pd.read_csv(io.StringIO(content_string))
            elif "xls" in filename:
                df = pd.read_excel(io.BytesIO(content_string))
        except Exception as e:
            print(e)
            return "There was an error processing this file.", None, None
        return filename, date, df.to_dict("records")
    if content_string is None:
        raise dash.exceptions.PreventUpdate
