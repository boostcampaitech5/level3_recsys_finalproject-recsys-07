import dash
from dash import dcc, html, dash_table
from assets.data import df_user, columns_u
from assets.figure import perflexity, ngram

dash.register_page(__name__)

cols = [{"name": "idx", "id": "user_id"}]
cols.extend([{"name": c, "id": c} for c in columns_u if "precision" in c])

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
                    [
                        dash_table.DataTable(
                            data=df_user.to_dict("records"),
                            columns=cols,
                            id="user-precision",
                            style_cell={
                                "textAlign": "left",
                                "padding": "10px 10px 10px 10px",
                            },
                            style_as_list_view=True,
                            style_data={
                                "whiteSpace": "normal",
                                "color": "black",
                                "backgroundColor": "white",
                                "height": "auto",
                            },
                            style_data_conditional=[],
                            style_header={
                                "backgroundColor": "rgb(210, 210, 210)",
                                "color": "black",
                                "fontWeight": "bold",
                            },
                            page_size=5,
                        ),
                    ],
                    style={
                        "grid-area": "1 / 6 / span 13 / span 7",
                        "overflow": "overlay",
                    },
                ),
                html.Div(
                    [
                        dcc.RangeSlider(0, 100, 10, value=[0, 100], id="da-slider"),
                        html.Div(id="da-slider-output"),
                    ],
                ),
                # 성공 실패 bar chart
                dcc.Graph(
                    id="sf-bar-chart",
                    className="fig",
                    style={"grid-area": "3 / 1 / span 15 / span 10"},
                ),
                dcc.RadioItems(  # 사용자 프로필 column 선택 버튼
                    options=[
                        {
                            "label": html.Span("성공", className="p-3 text-lg"),
                            "value": "Success",
                        },
                        {
                            "label": html.Span("실패", className="p-3 text-lg"),
                            "value": "Failure",
                        },
                    ],
                    value="Success",
                    id="sf-dialog-radio",
                    className="column-radio",
                    style={"grid-area": "2 / 1 / span 1 / span 4"},
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            # data=data.df_sentence.to_dict("records"),
                            columns=[
                                {"name": "idx", "id": "sentence_index"},
                                {"name": "sentence", "id": "sentence"},
                            ],
                            id="sf-dialog",
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
                                    "if": {"column_id": "sentence_index"},
                                    "max-width": "2vw",
                                    "min-width": "2vw",
                                },
                                {
                                    "if": {"column_id": "sentence"},
                                    "max-width": "35vw",
                                    "min-width": "35vw",
                                },
                            ],
                            style_header={
                                "backgroundColor": "rgb(210, 210, 210)",
                                "color": "black",
                                "fontWeight": "bold",
                            },
                            page_size=5,
                        ),
                    ],
                    style={
                        "grid-area": "1 / 6 / span 13 / span 7",
                        "overflow": "overlay",
                    },
                ),
                html.Div(
                    children=[
                        html.Span(" 사용자 ID : "),
                        dcc.Input(
                            id="da-user-id",
                            type="number",
                            placeholder="Search user-ID",
                            value=11,
                            style={
                                "font-weight": "bold",
                                "border": "solid 2px #ffdada",
                            },
                        ),
                    ],
                    className="p-4 fig f-3",
                    style={
                        "grid-area": "9 / 1 / span 1 / span 5",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "space-around",
                    },
                ),
                # 추천 효율 graph
                dcc.Graph(
                    id="da-graph",
                    className="fig",
                    style={"grid-area": "15 / 1 / span 15 / span 10"},
                ),
                html.Div(  # 소제목
                    "• 데이터 품질",
                    className="title p-4",
                    style={"grid-area": "10 / 1 / span 1 / span 4"},
                ),
                # perflexity graph
                dcc.Graph(
                    figure=perflexity(),
                    id="perflexity-dist",
                    className="fig",
                    style={"grid-area": "15 / 1 / span 15 / span 10"},
                ),
                # n-gram graph
                dcc.Graph(
                    figure=ngram(),
                    id="n-gram",
                    className="fig",
                    style={"grid-area": "15 / 1 / span 15 / span 10"},
                ),
                # dcc.Location(id="url"),
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="instance-grid",
        ),
    ],
    className="content no-scrollbar w-full",
)
