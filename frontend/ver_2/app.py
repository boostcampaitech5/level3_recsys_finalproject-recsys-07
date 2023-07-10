import os
import dash
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table, callback, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate
from assets import css

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
font_awsome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"
df = pd.read_csv('../../data/durecdial/dev_pp.csv')

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP,font_awsome,icons],
    use_pages=True,
    suppress_callback_exceptions=True,
)
sidebar_show = [
        dbc.Button(className='bi bi-list 2px',style={
            'margin-left':'0.5vw',
            'height':'5vh',
            'font-size':'1.5vw',
            'font-weight':'bold',    
            'align-items': 'center',
            'display': 'flex',
            'background-color':'transparent',
            'border':'transparent',
            'color':'#e4e3fa',
            },id='btn-sidebar'),
        
        dbc.Nav(
            [
                dbc.NavLink([html.Span(className='bi bi-house-door',style={'padding':'0vh 1vw'}),html.Span("Home")], href="/", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-columns',style={'padding':'0vh 1vw'}),html.Span("Description")], href="/description", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-bar-chart',style={'padding':'0vh 1vw'}),html.Span("qual-viz")], href="/qual-viz", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-card-text',style={'padding':'0vh 1vw'}),html.Span("quan-viz")], href="/quan-viz", active="exact",style=css.NAVSTYLE),
            ],
            # card=True,
            vertical=True,
            pills=False,
            style={
                'margin-left':'2vw',
                'align-items': 'left',
                'color':'#aeaeec',
                'font-weight': 'bold',
                'font-size': '1vw',
            }
        ),
    ]

sidebar_hidden = [
        dbc.Button(className='bi bi-list 2px',style={
            'height':'5vh',
            'margin-left':'0.5vw',
            'font-size':'1.5vw',
            'font-weight':'bold',    
            'align-items': 'center',
            'display': 'flex',
            'background-color':'transparent',
            'border':'transparent',
            'color':'#e4e3fa',
            },id='btn-sidebar'),
        
        dbc.Nav(
            [
                dbc.NavLink([html.Span(className='bi bi-house-door',style={'padding':'0vh 1vw'})], href="/", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-columns',style={'padding':'0vh 1vw'})], href="/description", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-bar-chart',style={'padding':'0vh 1vw'})], href="/qual-viz", active="exact",style=css.NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-card-text',style={'padding':'0vh 1vw'})], href="/quan-viz", active="exact",style=css.NAVSTYLE),
            ],
            # card=True,
            vertical=True,
            pills=False,
            style={
                'align-items': 'left',
                'color':'#aeaeec',
                'font-weight': 'bold',
                'font-size': '1vw',
            }
        ),
    ]

sidebar = html.Div(
    children = sidebar_show,
    style=css.SIDEBAR_STYLE,
    id='sidebar',
    # is_open=True,
    # backdrop=False,
)


navbar = dbc.NavbarSimple(
    children=[
        # dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
    ],
    brand="Dash4Chat",
    brand_href="",
    color="dark",
    dark=True,
    fluid=True,
    style=css.HEADER_STYLE,
)
layout_style = {
    'display': 'horizontal',
}
app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        html.Span([sidebar,
        dash.page_container,],style={'display':'flex'})
    ],
    style=layout_style
)

@app.callback(
    [
        Output("sidebar", "style"),
        Output("sidebar", "children"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn-sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = css.SIDEBAR_HIDDEN
            sidebar_children = sidebar_hidden
            content_style = css.CONTENT_SIDE_OFF
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = css.SIDEBAR_STYLE
            sidebar_children = sidebar_show
            content_style = css.CONTENT_SIDE_ON
            cur_nclick = "SHOW"
    else:
        sidebar_style = css.SIDEBAR_STYLE
        sidebar_children = sidebar_show
        content_style = css.CONTENT_SIDE_ON
        cur_nclick = 'SHOW'

    return sidebar_style, sidebar_children, content_style, cur_nclick

if __name__ == '__main__':
    app.run_server(debug=True, port=30002)