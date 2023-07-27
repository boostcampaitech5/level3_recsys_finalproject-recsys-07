import dash
from dash import html
from dash import dash_table
from assets.data import data_format

dash.register_page(__name__)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3(
                    children="📤 로그 데이터 업로드",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        "DashMon에 대화형 추천시스템의 로그데이터를 업로드하여 정량적, 정성적으로 분석할 수 있습니다.",
                        html.Br(),
                        "DashMon을 효과적으로 이용하기 위해 아래와 같은 포맷을 지켜 업로드해주세요.",
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
                html.H3(
                    children="📤 Dataset Format",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        html.A(
                            "예시 데이터셋 : DuRecDial2.0(EN)",
                            # href="../../data/durecdial/sample_data.csv",
                            className="text-lg font-bold",
                        ),
                        html.Br(),
                        " 데이터셋의 Feature(column)와 data type은 다음과 같습니다.",
                        dash_table.DataTable(
                            id="table",
                            columns=[{"name": i, "id": i} for i in data_format.columns],
                            data=data_format.to_dict("records"),
                            # export_format="csv",
                            style_table={"width": "80%"},
                            style_header={"font-weight": "bold"},
                            style_cell={"textAlign": "left"},
                        ),
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
            ],
        ),
        html.Div(className="p-8"),
    ],
    style={
        "display": "flex",
        "flex-direction": "column",
        "height": "93vh",
        "overflow": "scroll",
    },
    className="no-scrollbar",
)
