from dash import html, callback, Input, Output, State, Dash, dcc, dash_table
import dash_bootstrap_components as dbc
import base64
import datetime
import io, os
import pandas as pd
from urllib.parse import quote as urlquote



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
                children=['Upload Dataset🗃️'],
                style={
                    'margin-left' : '10%',
                    'margin-bottom' : '5%'
                }
                    ),
            dbc.NavLink(
                [
                    html.Span('README'),
                ],
                href="/readme",
                active="exact",
                className="side-nav",
            ),
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.A('Drag & Drop or Select File')
                ]),
                style={
                    'width': '70%',
                    'height': '50%',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin-left': '10%',
                    'margin-bottom' : '3%',
                    'font-size' : '15px'
                },
            ),
            html.Ul(id='file-list'),

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

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            df.to_dict('records'),
            [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])
