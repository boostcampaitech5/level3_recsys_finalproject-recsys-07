import dash
from dash import Dash, Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from assets import sidebar, data

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
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        ["DuRecDial2.0"], style={"font-size": 20}
                                    ),
                                    "value": "DuRecDial2.0",
                                },
                                {
                                    "label": html.Span(
                                        ["ReDial"], style={"font-size": 20}
                                    ),
                                    "value": "ReDial",
                                },
                            ],
                            value="DuRecDial2.0",
                            className="data-selector",
                            optionHeight=50,
                        )
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


@app.callback(
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
            sidebar_children = sidebar.sidebar_hidden
            content_className = "content content-side-hidden"
            cur_nclick = "HIDDEN"
        else:
            header_className = "header content-side-show"
            sidebar_className = "sidebar side-show"
            sidebar_children = sidebar.sidebar_show
            content_className = "content content-side-show"
            cur_nclick = "SHOW"
    else:
        header_className = "header content-side-show"
        sidebar_className = "sidebar side-show"
        sidebar_children = sidebar.sidebar_show
        content_className = "content content-side-show"
        cur_nclick = "SHOW"

    return (
        header_className,
        sidebar_className,
        sidebar_children,
        content_className,
        cur_nclick,
    )


@app.callback(
    Output("pie-chart", "figure"),
    Input("column-radio", "value"),
    Input("si-slider", "value"),
)
def draw_pie_chart(column, range):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
    """
    min_range = range[0]
    max_range = range[1]
    df = (
        data.df[[column]]
        .loc[
            (data.df["sentence_index"] >= min_range)
            & (data.df["sentence_index"] <= max_range)
        ]
        .value_counts()
        .to_frame()
    )
    df.columns = ["count"]
    df.reset_index(inplace=True)
    if df.shape[0] > 10:
        df.loc[9] = ["기타", df["count"].iloc[10:].sum()]
        df = df.iloc[:10]
    fig = go.Figure(data=[go.Pie(labels=df[column], values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )  # figure에서는 테두리를 둥글게 만들 수 없어서 배경색을 투명하게 설정.
    # fig.show()
    return fig


@app.callback(
    Output("bar-chart", "figure"),
    Input("column-radio", "value"),
    Input("si-slider", "value"),
)
def draw_bar_chart(column, range, horizontal=False):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
    horizontal : 가로 출력 여부
    """
    min_range = range[0]
    max_range = range[1]
    df = (
        data.df[[column]]
        .loc[
            (data.df["sentence_index"] >= min_range)
            & (data.df["sentence_index"] <= max_range)
        ]
        .value_counts()
        .to_frame()
        .reset_index()
    )
    df.columns = [column, "count"]
    if horizontal:
        fig = px.bar(df, x="count", y=column, orientation="h")
    else:
        fig = px.bar(df, x=column, y="count")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )  # figure에서는 테두리를 둥글게 만들 수 없어서 배경색을 투명하게 설정.
    return fig


# def draw_line_chart(column, min_range=0, max_range=50, smooth=True):
#     """
#     column : 출력 원하는 column명
#     min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
#     smooth : 그래프 부드럽게 그리는 여부
#     """
#     if smooth:
#         shape = "spline"
#     else:
#         shape = "linear"
#     df = data.df[[column, "sentence_index"]].value_counts().to_frame()
#     df.columns = ["count"]
#     df.reset_index(inplace=True)
#     df.sort_values(by=[column, "sentence_index"], inplace=True)
#     fig = px.line(
#         df, x="sentence_index", y="count", color="goal_type", line_shape=shape
#     )
#     # fig.show()
#     return fig

# 'user_id', 'user_profile_age_range', 'user_profile_name',
#    'user_profile_residence', 'user_profile_accepted_food',
#    'user_profile_accepted_movies', 'user_profile_accepted_music',
#    'user_profile_rejected_music', 'user_profile_gender',
#    'user_profile_accepted_celebrities', 'user_profile_accepted_movie',
#    'user_profile_reject', 'user_profile_rejected_movies',
#    'user_profile_occupation', 'user_profile_accepted_music.1',
#    'user_profile_accepted_poi', 'user_profile_favorite_news',
#    'user_profile_accepted_news', 'user_profile_poi',
@app.callback(
    Output("user-dialog", "data"),
    Output("user-name", "children"),
    Output("user-gender", "children"),
    Output("user-age", "children"),
    Output("user-residence", "children"),
    Output("user-occupation", "children"),
    # Output('user-place','children'),
    Input("user-id", "value"),
)
def get_user_info(user_id):
    user = data.df[data.df.user_id == user_id]
    return (
        user.to_dict("records"),
        user["user_profile_name"].iloc[0],
        user["user_profile_gender"].iloc[0],
        user["user_profile_age_range"].iloc[0],
        user["user_profile_residence"].iloc[0],
        user["user_profile_occupation"].iloc[0],
    )  # , user['user_profile_place'].iloc[0]


if __name__ == "__main__":
    app.run_server(debug=True, port=30002)
