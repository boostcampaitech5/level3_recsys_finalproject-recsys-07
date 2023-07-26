import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
import base64
import datetime
import io
import pandas as pd

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        html.Img(
            src="../assets/images/dashmon-high-resolution-color-logo.png",
            style={"max-width": "20%"},
        ),
        html.H1(
            children="Welcome to DASHMON!📊",
            className="blink",
            style={
                "font-weight": "bold",
                "margin-top": "3%",
                "line-height": "150%",
                "font-size": "200%",
            },
        ),
        html.H2(
            "DASHMON은 대화형 추천시스템에서 활용되는 데이터를 시각화하고 분석하는 모니터링 툴입니다.",
            style={"line-height": "200%"},
        ),
        html.Div(
            children=[
                html.H3(
                    children="💡 DASHMON의 목표",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        "대시몬은 추천이 포함된 대화형 데이터로부터 추천 성능에 관한 인사이트와 대화의 품질에 대한 인사이트를 동시에 제공하고자 합니다.",
                        html.Br(),
                        "또한, 대시몬은 다양한 Baseline CRS 모델의 성능 비교를 제공하여 ",
                        "Conversational Recommender System(CRS)을 개발하고 유지하는 데에 도움을 줍니다.",
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
                html.H3(
                    children="💡 DASHMON의 기능",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        "DASHMON은 크게 ",
                        html.A(
                            "Overview", href="overview", className="text-lg font-bold"
                        ),
                        ", ",
                        html.A(
                            "Instance", href="instance", className="text-lg font-bold"
                        ),
                        ", ",
                        html.A(
                            "Data Analysis",
                            href="dataanalysis",
                            className="text-lg font-bold",
                        ),
                        ", ",
                        html.A(
                            "Model Evaluation",
                            href="modelevaluation",
                            className="text-lg font-bold",
                        ),
                        " 네 페이지로 구성됩니다.",
                        html.Br(),
                        html.Br(),
                        html.A(
                            "Overview", href="overview", className="text-lg font-bold"
                        ),
                        "에서는 대상 데이터셋의 여러 속성들과 분포등을 확인할 수 있으며, ",
                        "페이지 중앙에 위치한 Slider를 조정하여 대화 시점에 따른 데이터의 분포를 확인할 수 있습니다.",
                        html.Br(),
                        html.Br(),
                        html.A(
                            "Instance", href="instance", className="text-lg font-bold"
                        ),
                        "에서는 데이터셋을 직접 확인할 수 있습니다. ",
                        "DuRecDial2.0 데이터셋의 경우 각 대화마다 User Profile 정보가 함께 주어지는데, ",
                        "해당 내용을 편하게 확인할 수 있도록 유저 정보와 대화 정보를 구분하여 제공합니다. ",
                        "또한 데이터를 확인할 때, 열을 선택할 수 있어 필요한 정보만 확인할 수 있습니다.",
                        html.Br(),
                        html.Br(),
                        html.A(
                            "Data Analysis",
                            href="dataanalysis",
                            className="text-lg font-bold",
                        ),
                        "에서는 Overview에서 얻지 못한 심층적인 정보를 얻을 수 있습니다. ",
                        "데이터셋에 포함되는 추천의 효과 및 효율, 대화형 데이터의 사용 품질 등을 막대 그래프와 그래프 자료구조 시각화를 통해 확인할 수 있으며, ",
                        "사용자 임베딩 시각화를 확인할 수 있습니다.",
                        html.Br(),
                        html.Br(),
                        html.A(
                            "Model Evaluation",
                            href="modelevaluation",
                            className="text-lg font-bold",
                        ),
                        "에서는 데이터셋을 CRS모델 학습에 활용했을 때의 정량적인 성능 지표를 확인할 수 있으며, "
                        "지표에 따른 모델별 순위를 확인할 수 있습니다.",
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
            ],
        ),
        html.Div(
            [
                dcc.Upload(
                    id="upload-data",
                    children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                    style={
                        "width": "100%",
                        "height": "60px",
                        "lineHeight": "60px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "margin": "10px",
                    },
                    # Allow multiple files to be uploaded
                    multiple=True,
                ),
                html.Div(id="output-data-upload"),
            ],
            className="side-header",
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


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return html.Div(
        [
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),
            dash_table.DataTable(
                df.to_dict("records"), [{"name": i, "id": i} for i in df.columns]
            ),
            html.Hr(),  # horizontal line
            # For debugging, display the raw contents provided by the web browser
            html.Div("Raw Content"),
            html.Pre(
                contents[0:200] + "...",
                style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
            ),
        ]
    )


@callback(
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children
