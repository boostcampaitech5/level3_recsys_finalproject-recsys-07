import dash
from dash import html
from dash import dash_table
from assets.data import data_format_short

dash.register_page(__name__)

def style_bold(data):
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
    return styles

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
                        "margin": "3% 0% 0% 2%",
                    },
                ),
                html.H4(
                    children=[
                        "DashMon에 대화형 추천시스템의 로그데이터를 업로드하여 정량적, 정성적으로 분석할 수 있습니다.",
                        html.Br(),
                        "DashMon을 효과적으로 이용하기 위해 아래 bold 처리된 feature를 꼭 포함해주세요.",
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
                html.H3(
                    children="📤 Dataset Format",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin": "3% 0% 0% 2%",
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
                            data=data_format_short.to_dict("records"),
                            columns=[
                                {"name": i, "id": i} for i in ["열 이름", "데이터 타입", "설명"]
                            ],
                            export_format="csv",
                            style_table={"width": "80%"},
                            style_header={"font-weight": "bold"},
                            style_cell={
                                "textAlign": "left",
                                "padding": "10px",
                            },
                            # style_as_list_view=True,
                            style_data={
                                "whiteSpace": "normal",
                                "color": "black",
                                "backgroundColor": "white",
                                "height": "auto",
                            },
                            tooltip_data=[
                                {
                                    "설명": {"value": str(row["예시"]), "type": "markdown"},
                                }
                                for row in data_format_short.to_dict("records")
                            ],
                            tooltip_delay=0,
                            tooltip_duration=None,
                        ),
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
            ],
        ),
        html.Div(className="p-8"),
    ],
    className="content no-scrollbar",
)
