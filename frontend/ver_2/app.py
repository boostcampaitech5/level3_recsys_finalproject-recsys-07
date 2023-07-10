import os
import dash
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, dash_table, callback, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
font_awsome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
icons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.1/font/bootstrap-icons.css"
df = pd.read_csv('../../data/durecdial/dev_pp.csv')

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP,font_awsome,icons],
    use_pages=True,
    # suppress_callback_exceptions=True,
)

header_style = {
    'height': '7vh',
    'width': '85vw',
    'background-color':'#6690ff',
    'display':'flex',
}

SIDEBAR_STYLE = {
    "height": '100vh',
    "width": "15vw",
    "background-color": "#463bfa",
    'color':'#e4e3fa',
    # "display": 'flex',
}

NAVSTYLE = {
    'color':'#aeaeec',
}

sidebar = html.Div(
    [
        html.Span([
            html.Button(className='bi bi-list 2px',style={
            # 'height':'5vh',
            'padding':'1vh 1vw',
            'font-size':'1.5vw',
            'font-weight':'bold',    
            'align-items': 'center',
            'display': 'flex',
            'background-color':'transparent',
            'border':'transparent',
            'color':'#e4e3fa',
            },id='toggle-sidebar'),
            html.Div("dash4chat",className="display-6",style={
            'height':'5vh',
            'padding':'1vh 1vw',
            'font-size':'1.5vw',
            'font-weight':'bold',
            'align-items': 'center',
            'display': 'flex',
        }),],style={
            'display':'flex',
            'background-color':'#1e22fe',
            'height':'7vh',
            'align-items': 'center',
        }),
        
        dbc.Nav(
            [
                dbc.NavLink([html.Span(className='bi bi-house-door',style={'padding':'0vh 1vw'}),html.Span("Home")], href="/", active="exact",style=NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-columns',style={'padding':'0vh 1vw'}),html.Span("Description")], href="/description", active="exact",style=NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-bar-chart',style={'padding':'0vh 1vw'}),html.Span("qual-viz")], href="/qual-viz", active="exact",style=NAVSTYLE),
                dbc.NavLink([html.Span(className='bi bi-card-text',style={'padding':'0vh 1vw'}),html.Span("quan-viz")], href="/quan-viz", active="exact",style=NAVSTYLE),
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
    ],
    style=SIDEBAR_STYLE,
    id='sidebar',
    # is_open=True,
    # backdrop=False,
)


header = html.Div(
    [
        # dbc.Nav(
        #     [
        #         dbc.NavLink("Home", href="/", active="exact"),
        #         dbc.NavLink("description", href="/description", active="exact"),
        #         dbc.NavLink("qual-viz", href="/qual-viz", active="exact"),
        #         dbc.NavLink("quan-viz", href="/quan-viz", active="exact"),
        #     ],
        #     # card=True,
        #     horizontal=True,
        #     pills=False,
        #     style={
        #         'width':'85vw',
        #         'justify-content': 'space-evenly',
        #     }
        # ),
        html.Hr(),
    ],
    style=header_style
)
layout_style = {
    'display': 'horizontal',
    
}
app.layout = html.Div(
    [
        html.Div([
            html.Span([
            sidebar,
            html.Div([header,
            dash.page_container])],style={'display':'flex'})
        ],
        style={
        }
        )
    ],
    style=layout_style
)

@app.callback(
    Output("sidebar", "is_open"),
    Input("toggle-sidebar", "n_clicks"),
    State("sidebar", "is_open"),
)
def toggle_offcanvas(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True, port=30002, host='0.0.0.0')