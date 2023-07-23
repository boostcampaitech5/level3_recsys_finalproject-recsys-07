import dash
from dash import html

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
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="instance-grid",
        ),
    ],
    className="content no-scrollbar",
)
