import dash
from dash import dash_table, html
from assets.data import get_model_eval

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
                    style={"grid-area": "2 / 1 / span 10 / span 12"},
                ),
                html.Div(  # 소제목
                    "• 모델 문장 생성 성능",
                    className="title p-4",
                    style={"grid-area": "12 / 1 / span 1 / span 4"},
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
            ],
            id="model-grid",
        ),
    ],
    className="content no-scrollbar",
)
