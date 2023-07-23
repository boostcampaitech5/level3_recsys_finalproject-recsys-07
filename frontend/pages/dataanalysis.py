import dash
from dash import dcc, html, dash_table

dash.register_page(__name__)

CONTENT_STYLE = {
    "width": "85vw",
    "padding": "2vh 1vw",
    "display": "flex",
}

FIGURE_BLANK = {
    "width": "23vw",
    "height": "20vh",
    "padding": "2vh 2vw",
    "background-color": "#ffffff",
    "font-weight": "bold",
    "margin": "1vh 1vw",
}
content = html.Div(
    [
        html.Div(["figure-4"], style=FIGURE_BLANK),
        html.Div(["figure-5"], style=FIGURE_BLANK),
        html.Div(["figure-6"], style=FIGURE_BLANK),
    ],
    style=CONTENT_STYLE,
)

layout_style = {
    # 'display': 'flex'
    "background-color": "#e6e7e9",
    "height": "95vh",
}

layout = html.Div(
    [
        # dcc.Location(id="url"),
        html.Div(
            [
                # 1. slider - train_sentence_xs.csv파일에 index 사용
                # 2. 성공, 실패 figure
                # 3. 성공 대화 data_table(추천한 대화+추천받은대화)
                # 4. 실패 대화 data_table(추천한 대화+추천받은대화)
            ]
        ),
        content,
    ],
    style=layout_style,
)
