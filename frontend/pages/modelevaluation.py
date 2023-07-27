import dash
import plotly.graph_objects as go
from dash import dash_table, html, dcc, callback, Input, Output
from assets.data import (
    get_model_eval,
    get_model_eval_percent,
    kbrd_result_conversation,
    kgsf_result_conversation,
    redial_result_conversation,
    insp_result_recommendation,
    kbrd_result_recommendation,
    redial_result_recommendation,
    kgsf_result_recommendation,
    gen_metric,
    rec_metric,
)


dash.register_page(__name__)

df_rec_p = get_model_eval_percent("Recommendation")
df_rec = get_model_eval("Recommendation")

df_conv_p = get_model_eval_percent("Conversation")
df_conv = get_model_eval("Conversation")


# 최댓값을 갖는 셀에 bold 스타일을 적용하는 함수
def generate_tooltip(column, value):
    if column == "Model":
        return value
    return f"{column} 최대값 대비 성능: {value}"


def style_minmax_cells(df):
    styles = []
    for c in range(1, len(df.columns)):
        cell_style = {
            "if": {
                "filter_query": f"{{{df.columns[c]}}} = {df.iloc[:,c].max()}",
                "column_id": df.columns[c],
            },
            "font-weight": "bold",
            "background-color": "#ffd6f1",
        }
        styles.append(cell_style)
    for c in range(1, len(df.columns)):
        cell_style = {
            "if": {
                "filter_query": f"{{{df.columns[c]}}} = {df.iloc[:,c].min()}",
                "column_id": df.columns[c],
            },
            "font-weight": "bold",
            "background-color": "#d6e2ff",
        }
        styles.append(cell_style)
    return styles


layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(  # 소제목
                            "모델 추천 성능",
                            className="title",
                        ),
                        html.Div(
                            [
                                dash_table.DataTable(
                                    # Conversation, Recommendation
                                    data=get_model_eval("Recommendation").to_dict(
                                        "records"
                                    ),
                                    columns=[
                                        {"name": c, "id": c}
                                        for c in [
                                            "Model",
                                            "Hit@1",
                                            "Hit@10",
                                            "Hit@50",
                                            "MRR@1",
                                            "MRR@10",
                                            "MRR@50",
                                            "NDCG@1",
                                            "NDCG@10",
                                            "NDCG@50",
                                        ]
                                    ],
                                    export_format="csv",
                                    id="rec-models",
                                    sort_action="native",
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
                                    style_data_conditional=style_minmax_cells(df_rec),
                                    style_header={
                                        "backgroundColor": "rgb(210, 210, 210)",
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                    tooltip_data=[
                                        {
                                            column: {
                                                "value": generate_tooltip(
                                                    column, value
                                                ),
                                                "type": "markdown",
                                            }
                                            for column, value in row.items()
                                        }
                                        for row in df_rec_p.to_dict("records")
                                    ],
                                    tooltip_delay=0,
                                    tooltip_duration=None,
                                    page_size=10,
                                ),
                            ],
                        ),
                    ],
                    className="section",
                ),
                html.Div(
                    [
                        html.Div(  # 소제목
                            "모델 문장 생성 성능",
                            className="title",
                        ),
                        html.Div(
                            [
                                dash_table.DataTable(
                                    data=get_model_eval("Conversation").to_dict(
                                        "records"
                                    ),
                                    columns=[
                                        {"name": c, "id": c}
                                        for c in [
                                            "Model",
                                            "BLEU@1",
                                            "BLEU@2",
                                            "BLEU@3",
                                            "BLEU@4",
                                            "Dist@1",
                                            "Dist@2",
                                            "Dist@3",
                                            "Dist@4",
                                            "Average",
                                            "Extreme",
                                            "Greedy",
                                            "PPL",
                                        ]
                                    ],
                                    id="conv-models",
                                    export_format="csv",

                                    sort_action="native",
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
                                    style_data_conditional=style_minmax_cells(df_conv),
                                    style_header={
                                        "backgroundColor": "rgb(210, 210, 210)",
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                    tooltip_data=[
                                        {
                                            column: {
                                                "value": generate_tooltip(
                                                    column, value
                                                ),
                                                "type": "markdown",
                                            }
                                            for column, value in row.items()
                                        }
                                        for row in df_conv_p.to_dict("records")
                                    ],
                                    tooltip_delay=0,
                                    tooltip_duration=None,
                                    page_size=10,
                                ),
                            ],
                            style={
                                # "grid-area": "13 / 1 / span 10 / span 12",
                                "transition": "all 0.5s"
                            },
                        ),
                    ],
                    className="section no-scrollbar",
                    style={
                        "overflow": "overlay",
                    },
                ),
                html.Div(
                    [
                        html.Div(  # 소제목
                            "모델 학습 로그",
                            className="title",
                        ),
                        html.Div(
                            [
                                dcc.RadioItems(
                                    options=[
                                        {
                                            "label": html.Span(
                                                m, className="p-3 text-lg"
                                            ),
                                            "value": m,
                                        }
                                        for m in rec_metric
                                    ],
                                    value="hit@1",
                                    id="rec-metric-radio",
                                    className="column-radio",
                                ),
                                dcc.Graph(
                                    id="rec-metric-figure",
                                    className="fig",
                                ),
                            ],
                            className="border-clear fig",
                        ),
                        html.Div(
                            [
                                dcc.RadioItems(
                                    options=[
                                        {
                                            "label": html.Span(
                                                m, className="p-3 text-lg"
                                            ),
                                            "value": m,
                                        }
                                        for m in gen_metric
                                    ],
                                    value="bleu@1",
                                    id="gen-metric-radio",
                                    className="column-radio",
                                ),
                                dcc.Graph(
                                    id="gen-metric-figure",
                                    className="fig",
                                ),
                            ],
                            className="border-clear fig",
                        ),
                    ],
                    className="section",
                ),
            ],
            id="model-grid",
        ),
    ],
    className="content no-scrollbar",
)


@callback(
    Output("gen-metric-figure", "figure"),
    Input("gen-metric-radio", "value"),
)
def gen_metric_figure(metric):
    # 'bleu@1', 'bleu@2', 'bleu@3', 'bleu@4', 'dist@1', 'dist@2', 'dist@3', 'dist@4'

    fig = go.Figure()
    min_val = (
        min(
            len(kbrd_result_conversation[metric]), len(kgsf_result_conversation[metric])
        )
        - 1
    )
    # Line Trace 추가
    fig.add_trace(
        go.Scatter(
            y=kbrd_result_conversation[metric][:min_val],
            mode="lines+markers",
            name="KBRD",
        )
    )
    fig.add_trace(
        go.Scatter(
            y=kgsf_result_conversation[metric][:min_val],
            mode="lines+markers",
            name="KGSF",
        )
    )
    fig.add_trace(
        go.Scatter(
            y=redial_result_conversation[metric][:min_val],
            mode="lines+markers",
            name="Redial",
        )
    )

    # 차트 레이아웃 설정
    fig.update_layout(title=f"{metric}", xaxis_title="Epoch", yaxis_title=f"{metric}")
    y_min = 0
    fig.update_yaxes(range=(y_min, None))

    # 차트 출력
    # fig.show()
    return fig


@callback(
    Output("rec-metric-figure", "figure"),
    Input("rec-metric-radio", "value"),
)
def rec_metric_figure(metric):
    fig = go.Figure()
    min_val = min(
        len(kbrd_result_recommendation[metric]), len(kgsf_result_recommendation[metric])
    )
    # Line Trace 추가
    fig.add_trace(
        go.Scatter(
            y=kbrd_result_recommendation[metric][:min_val],
            mode="lines+markers",
            name="KBRD",
        )
    )
    fig.add_trace(
        go.Scatter(
            y=kgsf_result_recommendation[metric][:min_val],
            mode="lines+markers",
            name="KGSF",
        )
    )

    fig.add_trace(
        go.Scatter(
            y=insp_result_recommendation[metric][:min_val],
            mode="lines+markers",
            name="Inspired",
        )
    )
    fig.add_trace(
        go.Scatter(
            y=redial_result_recommendation[metric][:min_val],
            mode="lines+markers",
            name="Redial",
        )
    )

    # 차트 레이아웃 설정
    fig.update_layout(title=f"{metric}", xaxis_title="Epoch", yaxis_title=f"{metric}")
    y_min = 0
    y_max = 1
    fig.update_yaxes(range=[y_min, y_max])

    y_min = 0
    fig.update_yaxes(range=(y_min, None))
    # 차트 출력
    # fig.show()
    return fig
