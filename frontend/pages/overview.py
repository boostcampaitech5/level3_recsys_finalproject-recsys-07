import dash
from assets import figure
from assets.data import df_sentence, size, max_si, user_count, columns, df_user
from dash import Input, Output, callback, dcc, html
import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            "데이터셋 개괄",
                            className="title",
                        ),
                    ],
                    className="col-start-1 col-end-5",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-clipboard-data round card-icon"),
                        html.Div(size, className="card-value"),
                        html.Div("Instances (Rows)"),
                    ],
                    className="figure-card border-clear",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-people-fill round card-icon"),
                        html.Div(children=[user_count], className="card-value"),
                        html.Div("Users"),
                    ],
                    className="figure-card border-clear",
                ),
                html.Div(
                    children=[
                        html.Div(
                            className="bi bi-layout-three-columns round card-icon",
                        ),
                        html.Div(len(columns), className="card-value"),
                        html.Div("Features (Columns)"),
                    ],
                    className="figure-card border-clear",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-chat-left-dots round card-icon"),
                        html.Div(
                            [
                                html.Div(
                                    len(df_sentence["goal_topic"].unique()),
                                    className="card-value",
                                ),
                                html.Div(
                                    len(df_sentence["goal_type"].unique()),
                                    className="card-value",
                                ),
                                html.Div("Topics"),
                                html.Div("Goal Types"),
                            ],
                            className="grid grid-cols-2 grid-rows-2",
                        ),
                    ],
                    className="figure-card border-clear",
                ),
            ],
            className="grid grid-cols-4 section",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div("대화 특성별 발화 분포 시각화", className="title"),
                    ],
                    className="col-start-1 col-end-7",
                ),
                html.Div(
                    children=[
                        html.Div(
                            [
                                dcc.Graph(
                                    # figure=figure.draw_pie_chart(
                                    #     df_sentence, "goal_type"
                                    # ),
                                    id="pie-chart",
                                    className="fig border-clear",
                                ),
                            ],
                            className="col-start-1 col-end-3 row-start-2 row-end-6",
                        ),
                        html.Div(
                            [
                                dcc.RangeSlider(
                                    0, max_si, 1, value=[0, 10], id="si-slider"
                                ),
                                html.Div(id="slider-output"),
                            ],
                            className="col-start-3 col-end-7 row-start-2 row-end-3 fig border-clear p-6",
                        ),
                        html.Div(
                            dcc.Graph(
                                # figure=figure.draw_bar_chart(df_user, "wday"),
                                className="fig border-clear",
                                id="bar-chart",
                            ),
                            className="col-start-3 col-end-7 row-start-3 row-end-7",
                        ),
                        html.Div(
                            dcc.RadioItems(
                                options=[
                                    {
                                        "label": html.Span(
                                            "시간", className="p-3 text-lg"
                                        ),
                                        "value": "time",
                                    },
                                    {
                                        "label": html.Span(
                                            "장소", className="p-3 text-lg"
                                        ),
                                        "value": "place",
                                    },
                                    {
                                        "label": html.Span(
                                            "날짜", className="p-3 text-lg"
                                        ),
                                        "value": "date",
                                    },
                                    {
                                        "label": html.Span(
                                            "주제", className="p-3 text-lg"
                                        ),
                                        "value": "topic",
                                    },
                                    {
                                        "label": html.Span(
                                            "요일", className="p-3 text-lg"
                                        ),
                                        "value": "wday",
                                    },
                                    {
                                        "label": html.Span(
                                            "발화 목적 (Goal Type)", className="p-3 text-lg"
                                        ),
                                        "value": "goal_type",
                                    },
                                ],
                                value="goal_type",
                                id="column-radio",
                                className="fig border-clear p-3 column-radio",
                            ),
                            className="col-start-1 col-end-3 row-start-6 row-end-7",
                        ),
                    ],
                    className="grid-cols-6 grid grid-row-6",
                ),
            ],
            className="section",
        ),
        html.Div(
            children=[
                html.Div("대화 진행에 따른 발화 의도 분포 시각화", className="title"),
                html.Div(
                    [
                        html.Div(
                            dcc.Graph(
                                figure=figure.draw_line_chart(df_sentence, "goal_type"),
                                className="fig border-clear",
                            ),
                            className="col-start-1 col-end-5",
                        ),
                        html.Div(
                            dcc.Graph(
                                figure=figure.draw_pie_chart(df_sentence, "goal_topic"),
                                className="fig border-clear",
                            ),
                            className="col-start-5 col-end-7",
                        ),
                    ],
                    className="grid grid-cols-6",
                ),
            ],
            className="section",
        ),
        html.Div(
            "Loading...",
            style={
                "padding": "20px",
            },
        ),
    ],
    className="content no-scrollbar flex flex-col",
)


@callback(
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


@callback(
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
