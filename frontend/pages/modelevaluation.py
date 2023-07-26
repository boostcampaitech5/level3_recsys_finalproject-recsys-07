import dash
from dash import dash_table, html, dcc, callback, Input, Output
from assets.data import get_model_eval
import plotly.graph_objects as go

dash.register_page(__name__)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(  # 소제목
                    "• 모델 추천 성능",
                    className="title p-4",
                    style={"grid-area": "1 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            # Conversation, Recommendation
                            data=get_model_eval("Recommendation"),
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
                            style_data_conditional=[
                                {
                                    "if": {"row_index": "odd"},
                                    "backgroundColor": "#f1f5f9",
                                }
                            ],
                            style_header={
                                "backgroundColor": "rgb(210, 210, 210)",
                                "color": "black",
                                "fontWeight": "bold",
                            },
                            page_size=10,
                        ),
                    ],
                ),
                dcc.Graph(
                    id="rec-metric-figure",
                    className="fig",
                ),
                html.Div(  # 소제목
                    "• 모델 문장 생성 성능",
                    className="title p-4",
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            data=get_model_eval("Conversation"),
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
                            style_data_conditional=[
                                {
                                    "if": {"row_index": "odd"},
                                    "backgroundColor": "#f1f5f9",
                                }
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
                        # "grid-area": "13 / 1 / span 10 / span 12",
                        "transition": "all 0.5s"
                    },
                ),
                dcc.Graph(
                    id="gen-metric-figure",
                    className="fig",
                ),
            ],
            id="model-grid",
        ),
    ],
    className="content no-scrollbar",
)

rec_metric = [
    "hit@1",
    "hit@10",
    "hit@50",
    "mrr@1",
    "mrr@10",
    "mrr@50",
    "ndcg@1",
    "ndcg@10",
    "ndcg@50",
]
conv_metric = [
    "bleu@1",
    "bleu@2",
    "bleu@3",
    "bleu@4",
    "dist@1",
    "dist@2",
    "dist@3",
    "dist@4",
]

kgsf_raw = [eval(t) for t in open("KGSF")]

kgsf_result_recommendation = {rm: list() for rm in rec_metric}
kgsf_result_conversation = {rm: list() for rm in conv_metric}

for kgsf in kgsf_raw:
    # recommendation
    if "hit@1" in kgsf:
        for k in kgsf:
            if k in kgsf_result_recommendation:
                kgsf_result_recommendation[k].append(kgsf[k])

    # conversation
    if "bleu@1" in kgsf:
        for k in kgsf:
            if k in kgsf_result_conversation:
                kgsf_result_conversation[k].append(kgsf[k])

kbrd_raw = [eval(t) for t in open("KBRD")]

kbrd_result_recommendation = {rm: list() for rm in rec_metric}
kbrd_result_conversation = {rm: list() for rm in conv_metric}

for kbrd in kbrd_raw:
    # recommendation
    if "hit@1" in kbrd:
        for k in kbrd:
            if k in kbrd_result_recommendation:
                kbrd_result_recommendation[k].append(kbrd[k])

    # conversation
    if "bleu@1" in kbrd:
        for k in kbrd:
            if k in kbrd_result_conversation:
                kbrd_result_conversation[k].append(kbrd[k])

insp_raw = [eval(t) for t in open("insp")]

insp_result_recommendation = {rm: list() for rm in rec_metric}
insp_result_conversation = {rm: list() for rm in conv_metric}

for insp in insp_raw:
    # recommendation
    if "hit@1" in insp:
        for k in insp:
            if k in insp_result_recommendation:
                insp_result_recommendation[k].append(insp[k])

    # conversation
    if "bleu@1" in insp:
        for k in insp:
            if k in insp_result_conversation:
                insp_result_conversation[k].append(insp[k])

redial_raw = [eval(t) for t in open("Redial")]

redial_result_recommendation = {rm: list() for rm in rec_metric}
redial_result_conversation = {rm: list() for rm in conv_metric}

for redial in redial_raw:
    # recommendation
    if "hit@1" in redial:
        for k in redial:
            if k in redial_result_recommendation:
                redial_result_recommendation[k].append(redial[k])

    # conversation
    if "bleu@1" in redial:
        for k in redial:
            if k in redial_result_conversation:
                redial_result_conversation[k].append(redial[k])


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
    fig.show()
