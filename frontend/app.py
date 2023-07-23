import dash
from dash import Dash, Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import networkx as nx
import plotly.graph_objects as go
from assets import sidebar
from assets.data import df_user, df_sentence

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
    if column in ["wday", "topic", "date", "place", "time"]:
        df = (
            df_user[[column]]
            .loc[
                (df_sentence["sentence_index"] >= min_range)
                & (df_sentence["sentence_index"] <= max_range)
            ]
            .value_counts()
            .to_frame()
        )
    else:
        df = (
            df_sentence[[column]]
            .loc[
                (df_sentence["sentence_index"] >= min_range)
                & (df_sentence["sentence_index"] <= max_range)
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


@app.callback(Output("user-pie-chart", "figure"), Input("user-column-radio", "value"))
def draw_user_pie_chart(column):
    """
    column: 출력 원하는 column명
    """
    df = df_user[column].value_counts().to_frame()
    df.columns = ["count"]

    fig = go.Figure(data=[go.Pie(labels=df.index.to_list(), values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")  # 제목

    # fig.show()
    # age_range, gender, occupation, reject
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
    if column in ["wday", "topic", "date", "place", "time"]:
        df = (
            df_user[[column]]
            .loc[
                (df_sentence["sentence_index"] >= min_range)
                & (df_sentence["sentence_index"] <= max_range)
            ]
            .value_counts()
            .to_frame()
            .reset_index()
        )
    else:
        df = (
            df_sentence[[column]]
            .loc[
                (df_sentence["sentence_index"] >= min_range)
                & (df_sentence["sentence_index"] <= max_range)
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
#     df = df[[column, "sentence_index"]].value_counts().to_frame()
#     df.columns = ["count"]
#     df.reset_index(inplace=True)
#     df.sort_values(by=[column, "sentence_index"], inplace=True)
#     fig = px.line(
#         df, x="sentence_index", y="count", color="goal_type", line_shape=shape
#     )
#     # fig.show()
#     return fig


# name gender age residence occupation place


@app.callback(
    Output("user-dialog", "data"),
    Output("raw-data", "data"),
    Output("user-name", "children"),
    Output("user-gender", "children"),
    Output("user-age", "children"),
    Output("user-residence", "children"),
    Output("user-occupation", "children"),
    Output("user-food+", "children"),
    Output("user-movies+", "children"),
    Output("user-movies-", "children"),
    Output("user-movie+", "children"),
    Output("user-music1+", "children"),
    Output("user-music2+", "children"),
    Output("user-music-", "children"),
    Output("user-celebrity+", "children"),
    Output("user-reject", "children"),
    Output("user-poi+", "children"),
    Output("user-poi", "children"),
    Output("user-news+", "children"),
    Output("user-news", "children"),
    Input("inst-user-id", "value"),
)
def get_user_info(user_id):
    user = df_user[df_user.user_id == user_id]
    sentence = df_sentence[df_sentence.user_id == user_id]
    return (
        sentence.to_dict("records"),
        sentence.to_dict("records"),
        user["user_profile_name"].iloc[0],
        user["user_profile_gender"].iloc[0],
        user["user_profile_age_range"].iloc[0],
        user["user_profile_residence"].iloc[0],
        user["user_profile_occupation"].iloc[0],
        user["user_profile_accepted_food"].iloc[0],
        user["user_profile_accepted_movies"].iloc[0],
        user["user_profile_rejected_movies"].iloc[0],
        user["user_profile_accepted_movie"].iloc[0],
        user["user_profile_accepted_music"].iloc[0],
        user["user_profile_accepted_music.1"].iloc[0],
        user["user_profile_rejected_music"].iloc[0],
        user["user_profile_accepted_celebrities"].iloc[0],
        user["user_profile_reject"].iloc[0],
        user["user_profile_accepted_poi"].iloc[0],
        user["user_profile_poi"].iloc[0],
        user["user_profile_favorite_news"].iloc[0],
        user["user_profile_accepted_news"].iloc[0],
    )


@app.callback(
    Output("raw-data", "columns"),
    Input("column-list", "value"),
)
def get_selected_column(column_list):
    return [{"name": c, "id": c} for c in column_list]


@app.callback(
    Output("sf-dialog", "data"),
    Input("sf-dialog-radio", "value"),
)
def get_sf_dialog(val):
    return df_sentence[df_sentence.recommend_sf == val].to_dict("records")


@app.callback(
    Output("sf-bar-chart", "figure"),
    Input("da-slider", "value"),
)
def draw_recommend_sf_chart(slider, column="recommend_sf"):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 index 범위(시간의 범위), 기본값 [0, 100]
    """
    min_range = slider[0]
    max_range = slider[1]

    # 라벨
    top_labels = ["Success", "Failure"]

    # 차트 색깔
    colors = [px.colors.qualitative.Plotly, px.colors.qualitative.Plotly[1]]

    # 데이터
    if column in df_user.columns:
        value_counts = df_user[column][
            min_range : max_range + 1  # noqa: E203
        ].value_counts()
    else:
        value_counts = df_sentence[column][
            min_range : max_range + 1  # noqa: E203
        ].value_counts()
    total_count = value_counts.sum()
    df_percentage = value_counts / total_count * 100
    x_data = [[df_percentage[0].round(1), df_percentage[1].round(1)]]
    # id값(아직 보이게 설정안함)
    y_data = ["success_failure Distribution"]

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(
                go.Bar(
                    x=[xd[i]],
                    y=[yd],
                    orientation="h",
                    marker=dict(
                        color=colors[i], line=dict(color="rgb(248, 248, 249)", width=1)
                    ),
                )
            )

    fig.update_layout(
        title=dict(
            text=f"{y_data[0]}",
            font=dict(size=36),
            x=0.5,
            pad=dict(b=1000, t=1000),
        ),
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode="stack",
        paper_bgcolor="rgb(248, 248, 255)",
        plot_bgcolor="rgb(248, 248, 255)",
        showlegend=False,
        margin=dict(t=140, b=80),
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the first percentage of each bar (x_axis)
        annotations.append(
            dict(
                xref="x",
                yref="y",
                x=xd[0] / 2,
                y=yd,
                text=str(xd[0]) + "%",
                font=dict(family="Arial", size=20, color="rgb(248, 248, 255)"),
                showarrow=False,
            )
        )
        # labeling the first Likert scale (on the top)
        annotations.append(
            dict(
                xref="x",
                yref="paper",
                x=xd[0] / 2,
                y=1.1,
                text=top_labels[0],
                font=dict(family="Arial", size=20, color="rgb(67, 67, 67)"),
                showarrow=False,
            )
        )
        space = xd[0]
        for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(
                dict(
                    xref="x",
                    yref="y",
                    x=space + (xd[i] / 2),
                    y=yd,
                    text=str(xd[i]) + "%",
                    font=dict(family="Arial", size=20, color="rgb(248, 248, 255)"),
                    showarrow=False,
                )
            )
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(
                    dict(
                        xref="x",
                        yref="paper",
                        x=space + (xd[i] / 2),
                        y=1.1,
                        text=top_labels[i],
                        font=dict(family="Arial", size=20, color="rgb(67, 67, 67)"),
                        showarrow=False,
                    )
                )
            space += xd[i]

    fig.update_layout(annotations=annotations)
    # fig.show()
    return fig


@app.callback(
    Output("da-graph", "figure"),
    Input("da-user-id", "value"),
)
def draw_graph(
    user_id,
    with_labels=False,
    node_size=400,
    width=2,
    style=None,
    draw=False,
    return_graph=False,
):
    """
    with_labels : node에 index 표시
    -x- node_size : node 크기
    -x- width : edge 두께
    style : 그래프 스타일 ('circular', 'spectral', 'kamada_kawai', 'planar', 'spring', 'shell')
    -x- draw : 그래프 표시
    -x- return_graph : 반환 값을 graph로 변경. False일 시 대화 시작부터 종료까지 길이를 반환
    """
    G = nx.Graph()

    color_map = []
    before = 0
    flag = False
    cdf = df_sentence[df_sentence.user_id == user_id]

    for i in range(cdf.shape[0]):
        log = cdf.iloc[i]
        if log.is_user:
            color_map.append("blue")
        else:
            color_map.append("red")
        G.add_node(i)
        if i == 0:
            continue
        if log.is_user:
            G.add_edge(i, i - 1)
            if log.deny:
                flag = True
            else:
                flag = False
                before = i
        else:
            if flag:
                G.add_edge(i, before)
            else:
                G.add_edge(i, i - 1)
    color_map[0], color_map[-1] = "black", "gray"

    pos = nx.spring_layout(G)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        hoverinfo="none",
        marker=dict(color=color_map, showscale=False, size=10, line_width=2),
    )

    # layout
    layout = dict(
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(t=10, b=10, l=10, r=10, pad=0),
        showlegend=False,
        xaxis=dict(
            linecolor="black", showgrid=False, showticklabels=False, mirror=True
        ),
        yaxis=dict(
            linecolor="black", showgrid=False, showticklabels=False, mirror=True
        ),
    )

    # figure
    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
    return fig


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=30005)
