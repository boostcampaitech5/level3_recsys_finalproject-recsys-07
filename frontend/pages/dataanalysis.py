import dash
from assets.data import columns_u
from assets.figure import perflexity, ngram
from dash import Input, Output, callback, dash_table, dcc, html
import plotly.express as px
import networkx as nx
import plotly.graph_objects as go
from assets.data import df_user, df_sentence

dash.register_page(__name__)

cols = [{"name": "idx", "id": "user_id"}]
cols.extend([{"name": c, "id": c} for c in columns_u if "precision" in c])

layout = html.Div(
    [
        html.Div(
            [
                html.Div(  # 소제목
                    "• 추천 효과 및 효율",
                    className="title p-4",
                    style={"grid-area": "1 / 1 / span 1 / span 5"},
                ),
                html.Div(
                    children=[
                        html.Span(" 사용자 ID : "),
                        dcc.Input(
                            id="da-user-id",
                            type="number",
                            placeholder="Search user-ID",
                            value=12,
                            style={
                                "font-weight": "bold",
                                "border": "solid 2px #ffdada",
                            },
                        ),
                    ],
                    className="p-4 fig f-3",
                    style={
                        "grid-area": "2 / 1 / span 1 / span 4",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "space-around",
                    },
                ),
                html.Div(
                    [
                        html.Div("precision", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@5", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-5",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@1", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-1",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@6", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-6",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@2", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-2",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@7", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-7",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@3", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-3",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@8", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-8",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@4", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-4",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@9", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-9",
                            className="user-info col-start-4 col-end-5",
                        ),
                    ],
                    className="fig",
                    style={
                        "display": "grid",
                        "grid-area": "3 / 1 / span 5 / span 4",
                        "grid-template-columns": "2fr 4fr 2fr 4fr",
                        "grid-template-rows": "repeat(6, minmax(0, 1fr))",
                        "row-gap": "2rem",
                        "padding": "2rem",
                        "justify-items": "start",
                        "align-items": "center",
                    },
                ),
                # 추천 효율 graph
                dcc.Graph(
                    id="da-graph",
                    className="fig",
                    style={"grid-area": "1 / 5 / span 6 / span 8"},
                ),
                html.Div(
                    [
                        dcc.RangeSlider(0, 100, 10, value=[0, 100], id="da-slider"),
                    ],
                    style={
                        "grid-area": "8 / 1 / span 1 / span 5",
                    },
                    className="fig p-6",
                ),
                # 성공 실패 bar chart
                dcc.Graph(
                    id="sf-bar-chart",
                    className="fig",
                    style={"grid-area": "9 / 1 / span 7 / span 5"},
                ),
                dcc.RadioItems(  # 사용자 프로필 column 선택 버튼
                    options=[
                        {
                            "label": html.Span("성공", className="p-3 text-lg"),
                            "value": "Success",
                        },
                        {
                            "label": html.Span("실패", className="p-3 text-lg"),
                            "value": "Failure",
                        },
                    ],
                    value="Success",
                    id="sf-dialog-radio",
                    className="column-radio",
                    style={"grid-area": "7 / 6 / span 1 / span 7"},
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            # data=data.df_sentence.to_dict("records"),
                            columns=[
                                {"name": "idx", "id": "sentence_index"},
                                {"name": "sentence", "id": "sentence"},
                            ],
                            id="sf-dialog",
                            style_cell={
                                "textAlign": "left",
                                "padding": "10px 10px 10px 30px",
                            },
                            style_as_list_view=True,
                            style_data={
                                "whiteSpace": "normal",
                                "color": "black",
                                "backgroundColor": "white",
                                "height": "auto",
                            },
                            style_data_conditional=[
                                {
                                    "if": {"column_id": "sentence_index"},
                                    "max-width": "2vw",
                                    "min-width": "2vw",
                                },
                                {
                                    "if": {"column_id": "sentence"},
                                    "max-width": "25vw",
                                    "min-width": "25vw",
                                },
                            ],
                            style_header={
                                "backgroundColor": "rgb(210, 210, 210)",
                                "color": "black",
                                "fontWeight": "bold",
                            },
                            page_size=10,
                        ),
                    ],
                    style={
                        "grid-area": "8 / 6 / span 9 / span 7",
                        "overflow": "overlay",
                    },
                ),
                html.Div(  # 소제목
                    "• 데이터 품질",
                    className="title p-4",
                    style={"grid-area": "17 / 1 / span 1 / span 4"},
                ),
                # perflexity graph
                dcc.Graph(
                    figure=perflexity(),
                    id="perflexity-dist",
                    className="fig",
                    style={"grid-area": "18 / 1 / span 12 / span 6"},
                ),
                # n-gram graph
                dcc.Graph(
                    figure=ngram(),
                    id="n-gram",
                    className="fig",
                    style={"grid-area": "18 / 7 / span 12 / span 6"},
                ),
                # dcc.Location(id="url"),
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="da-grid",
        ),
    ],
    className="content no-scrollbar",
)


@callback(
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


@callback(
    Output("sf-dialog", "data"),
    Input("sf-dialog-radio", "value"),
    Input("da-slider", "value"),
)
def get_sf_dialog(val, slider):
    return df_sentence[df_sentence.recommend_sf == val][
        slider[0] : slider[1]  # noqa:E203
    ].to_dict("records")


@callback(
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
            font=dict(size=18),
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
        paper_bgcolor="rgb(255, 255, 255)",
        plot_bgcolor="rgb(255, 255, 255)",
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


@callback(
    Output("precision-value", "children"),
    Output("precision-value-1", "children"),
    Output("precision-value-2", "children"),
    Output("precision-value-3", "children"),
    Output("precision-value-4", "children"),
    Output("precision-value-5", "children"),
    Output("precision-value-6", "children"),
    Output("precision-value-7", "children"),
    Output("precision-value-8", "children"),
    Output("precision-value-9", "children"),
    Input("da-user-id", "value"),
)
def get_user_precision(user_id):
    user = df_user[df_user.user_id == user_id]
    return (
        user["precision"].iloc[0].round(3),
        user["precision_1"].iloc[0].round(3),
        user["precision_2"].iloc[0].round(3),
        user["precision_3"].iloc[0].round(3),
        user["precision_4"].iloc[0].round(3),
        user["precision_5"].iloc[0].round(3),
        user["precision_6"].iloc[0].round(3),
        user["precision_7"].iloc[0].round(3),
        user["precision_8"].iloc[0].round(3),
        user["precision_9"].iloc[0].round(3),
    )
