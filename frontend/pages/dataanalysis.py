import dash
from dash import dcc, html, dash_table

dash.register_page(__name__)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(  # 소제목
                    "• 추천 효과 및 효율",
                    className="title p-4",
                    style={"grid-area": "1 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    # 성공 실패 bar chart
                ),
                html.Div(
                    # 추천 효율 graph
                ),
                html.Div(  # 소제목
                    "• 데이터 품질",
                    className="title p-4",
                    style={"grid-area": "10 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    # perflexity graph
                    id="perflexity",
                ),
                html.Div(
                    # n-gram graph
                    id="n-gram",
                ),
                      # dcc.Location(id="url"),
                html.Div(
                    [
                        # 1. slider - train_sentence_xs.csv파일에 index 사용
                        # 2. 성공, 실패 figure
                        # 3. 성공 대화 data_table(추천한 대화+추천받은대화)
                        # 4. 실패 대화 data_table(추천한 대화+추천받은대화)
                    ]
                ),
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="instance-grid",
        ),
    ],
    className="content no-scrollbar",
)
