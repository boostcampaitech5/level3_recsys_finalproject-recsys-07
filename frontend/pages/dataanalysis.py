import dash
from dash import dcc, html

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
                dcc.RadioItems(  # 사용자 프로필 column 선택 버튼
                    options=[
                        {
                            "label": html.Span("나이", className="p-3 text-lg"),
                            "value": "user_profile_age_range",
                        },
                        {
                            "label": html.Span("성별", className="p-3 text-lg"),
                            "value": "user_profile_gender",
                        },
                        {
                            "label": html.Span("고용상태", className="p-3 text-lg"),
                            "value": "user_profile_occupation",
                        },
                        {
                            "label": html.Span("대화 목표", className="p-3 text-lg"),
                            "value": "goal_type",
                        },
                        {
                            "label": html.Span("대화 주제", className="p-3 text-lg"),
                            "value": "goal_topic",
                        },
                        {
                            "label": html.Span("문장", className="p-3 text-lg"),
                            "value": "sentence",
                        },
                    ],
                    value="user_profile_gender",
                    id="sf-column-radio",
                    className="column-radio",
                    style={"grid-area": "2 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    [
                        dcc.RangeSlider(0, 20, 1, value=[0, 100], id="da-slider"),
                        html.Div(id="da-slider-output"),
                    ],
                ),
                html.Div(
                    # 성공 실패 bar chart
                    # 1. slider - train_sentence_xs.csv파일에 index 사용
                    # 2. 성공, 실패 figure
                    # 3. 성공 대화 data_table(추천한 대화+추천받은대화)
                    # 4. 실패 대화 data_table(추천한 대화+추천받은대화)
                    dcc.Graph(
                        id="sf-bar-chart",
                        className="fig",
                        style={"grid-area": "3 / 1 / span 15 / span 10"},
                    ),
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
            ],
            # className="grid grid-cols-12 grid-rows-36",
            id="instance-grid",
        ),
    ],
    className="content no-scrollbar",
)
