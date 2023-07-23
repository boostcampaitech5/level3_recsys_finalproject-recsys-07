import dash
from dash import dash_table, html
from assets.data import model_eval

dash.register_page(__name__)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(  # 소제목
                    "• 모델 성능 확인하기",
                    className="title p-4",
                    style={"grid-area": "1 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            data=model_eval.to_dict("records"),
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
                                    "Conversation",
                                    "Policy",
                                    "Recommendation",
                                ]
                            ],
                            id="models",
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
                    style={"grid-area": "21 / 1 / span 17 / span 12"},
                ),
            ],
        ),
    ],
    className="content no-scrollbar",
)
