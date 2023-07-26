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
                children=html.Div("Drag & Drop or Select File"),
                id="upload-data",
                className="upload-btn",
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
            # html.Ul(id="file-list"),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door side-nav-icon",
                    ),
                    html.Span("OVERVIEW"),
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
                    html.Span("INSTANCE"),
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
                    html.Span("DATA ANALYSIS"),
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
                    html.Span("MODEL EVALUATION"),
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
def update_data_store(content_string, filename, date):
    if content_string is not None:
        print("uploaded file: ", filename)
        try:
            if "csv" in filename:
                df = pd.read_csv(io.StringIO(content_string))
                print("csv 데이터파일 읽는 중...")
            elif "xls" in filename:
                df = pd.read_excel(io.BytesIO(content_string))
        except Exception as e:
            print(e)
            return "There was an error processing this file.", None, None
        return filename, date, df.to_dict("records")
    if content_string is None:
        raise dash.exceptions.PreventUpdate


@callback(
    Output("upload-progress-alert", "is_open"),
    Input("upload-data", "filename"),
)
def update_progress_alert(filename):
    if filename:
        return True
