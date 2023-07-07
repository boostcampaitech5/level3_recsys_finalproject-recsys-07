import os
import dash
from dash import Dash, dcc, html, Input, Output, dash_table, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate

# dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# font_awsome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.2/css/all.min.css"
app = Dash(
    __name__, 
    # external_stylesheets=[dbc.themes.JOURNAL, font_awsome],
    # use_pages=False,
    # suppress_callback_exceptions=True,
) # 페이지 스타일 변경


# username = 'mkdir'
# load_figure_template("journal") # figure 스타일 변경

app.layout = html.Div([
    html.Div(children="Hello World!"),
    # dcc.Store(id='store_user_state', storage_type='session'),
    # dcc.Store(id='store_user_dataset', storage_type='session'),
	# dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True, port=30002, host='0.0.0.0')