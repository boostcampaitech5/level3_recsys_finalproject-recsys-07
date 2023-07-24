import dash
from dash import dcc, html, dash_table
from assets.data import columns_u
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
                    style={"grid-area": "1 / 1 / span 1 / span 5"},
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
                        "grid-area": "1 / 5 / span 1 / span 4",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "space-around",
                    },
                ),
                html.Div(
                    [
                        html.Div("precision", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@5", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-5",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@1", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-1",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@6", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-6",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@2", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-2",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@7", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-7",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@3", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-3",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@8", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-8",
                            className="user-info col-start-4 col-end-5",
                        ),
                        html.Div("precision@4", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-4",
                            className="user-info col-start-2 col-end-3",
                        ),
                        html.Div("precision@9", className="col-start-3 col-end-4 p-2"),
                        html.Div(
                            children=[],
                            id="precision-value-9",
                            className="user-info col-start-4 col-end-5",
                        ),
                    ],
                    className="fig",
                    style={
                        "display": "grid",
                        "grid-area": "2 / 1 / span 5 / span 4",
                        "grid-template-columns": "2fr 4fr 2fr 4fr",
                        "grid-template-rows": "repeat(6, minmax(0, 1fr))",
                        "row-gap": "2rem",
                        "padding": "2rem",
                        "justify-items": "start",
                        "align-items": "center",
                    },
                ),
                # 추천 효율 graph
                dcc.Graph(
                    id="da-graph",
                    className="fig",
                    style={"grid-area": "1 / 5 / span 6 / span 8"},
                ),
                html.Div(
                    [
                        dcc.RangeSlider(0, 100, 10, value=[0, 100], id="da-slider"),
                    ],
                    style={
                        "grid-area": "8 / 1 / span 1 / span 5",
                    },
                    className="fig p-6",
                ),
                # 성공 실패 bar chart
                dcc.Graph(
                    id="sf-bar-chart",
                    className="fig",
                    style={"grid-area": "9 / 1 / span 7 / span 5"},
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
                    style={"grid-area": "7 / 6 / span 1 / span 7"},
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
                                    "max-width": "25vw",
                                    "min-width": "25vw",
                                },
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
                        "grid-area": "8 / 6 / span 9 / span 7",
                        "overflow": "overlay",
                    },
                ),
                html.Div(  # 소제목
                    "• 데이터 품질",
                    className="title p-4",
                    style={"grid-area": "17 / 1 / span 1 / span 4"},
                ),
                # perflexity graph
                dcc.Graph(
                    figure=perflexity(),
                    id="perflexity-dist",
                    className="fig",
                    style={"grid-area": "18 / 1 / span 12 / span 6"},
                ),
                # n-gram graph
                dcc.Graph(
                    figure=ngram(),
                    id="n-gram",
                    className="fig",
                    style={"grid-area": "18 / 7 / span 12 / span 6"},
                ),
                # dcc.Location(id="url"),
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="da-grid",
        ),
    ],
    className="content no-scrollbar",
)
