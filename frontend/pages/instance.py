import dash
from dash import html, dcc, dash_table
from assets import data, figure

dash.register_page(__name__)

opts = [{"label": "sentence_index", "value": "sentence_index", "disabled": True}]
opts.extend(
    [
        {"label": c, "value": c}
        for c in [
            "time",
            "place",
            "date",
            "topic",
            "wday",
            "goal_topic",
            "goal_type",
            "knowledge",
            "recdial",
        ]
    ]
)
layout = html.Div(
    children=[
        html.Div(
            children=[
                # 좌측에 표시할 정보
                html.Div(
                    children=[
                        # title
                        html.Div(
                            children=[
                                html.Div(
                                    "• 사용자 그룹 별 대화 주제 분석",
                                    className="row-start-1 row-end-2 card-value title",
                                ),
                                dcc.RadioItems(
                                    options=[
                                        {
                                            "label": html.Span(
                                                "나이", className="p-3 text-lg"
                                            ),
                                            "value": "user_profile_age_range",
                                        },
                                        {
                                            "label": html.Span(
                                                "성별", className="p-3 text-lg"
                                            ),
                                            "value": "user_profile_gender",
                                        },
                                        {
                                            "label": html.Span(
                                                "고용상태", className="p-3 text-lg"
                                            ),
                                            "value": "user_profile_occupation",
                                        },
                                        # {
                                        #     "label": html.Span(
                                        #         "reject", className="p-3 text-lg"
                                        #     ),
                                        #     "value": "user_profile_reject",
                                        # },
                                    ],
                                    value="user_profile_gender",
                                    id="user-column-radio",
                                    className="fig p-4 column-radio row-start-2 row-end-3",
                                ),
                            ],
                            className="row-start-1 row-end-2 grid grid-rows-2",
                        ),
                        # pie-chart
                        html.Div(
                            [
                                # age_range, gender, occupation, reject
                                dcc.Graph(
                                    figure=figure.draw_user_pie_chart(
                                        data.df_user, "user_profile_gender"
                                    ),
                                    id="user-pie-chart",
                                    className="fig",
                                ),
                                # input
                                html.Div(
                                    children=[
                                        html.H1(children=["Instance Index✏️"]),
                                        dcc.Input(
                                            id="user-id",
                                            type="number",
                                            placeholder="Search user-ID",
                                            value=5,
                                        ),
                                    ],
                                    className="row-start-2 row-end-3 p-4 fig",
                                ),
                            ],
                            className="row-start-2 row-end-4",
                        ),
                        # user-info
                        html.Div(
                            # name gender age residence occupation place
                            children=[
                                html.Div("name", className="col-start-1 col-end-2 p-2"),
                                html.Div(
                                    children=[],
                                    id="user-name",
                                    className="user-info col-start-2 col-end-3 p-2",
                                ),
                                html.Div(
                                    "gender", className="col-start-1 col-end-2 p-2"
                                ),
                                html.Div(
                                    children=[],
                                    id="user-gender",
                                    className="user-info col-start-2 col-end-3 p-2",
                                ),
                                html.Div("age", className="col-start-1 col-end-2 p-2"),
                                html.Div(
                                    children=[],
                                    id="user-age",
                                    className="user-info col-start-2 col-end-3 p-2",
                                ),
                                html.Div(
                                    "residence", className="col-start-1 col-end-2 p-2"
                                ),
                                html.Div(
                                    children=[],
                                    id="user-residence",
                                    className="user-info col-start-2 col-end-3 p-2",
                                ),
                                html.Div(
                                    "occupation", className="col-start-1 col-end-2 p-2"
                                ),
                                html.Div(
                                    children=[],
                                    id="user-occupation",
                                    className="user-info col-start-2 col-end-3 p-2",
                                ),
                            ],
                            className="row-start-5 row-end-7 grid grid-rows-3 grid-cols-2 fig p-4",
                        ),
                    ],
                    className="col-start-1 col-end-3 row-start-1 row-end-7 grid grid-rows-6",
                ),
                html.Div(
                    children=[
                        html.Div(
                            dash_table.DataTable(
                                data=data.df_sentence.to_dict("records"),
                                columns=[
                                    {"name": c, "id": c}
                                    for c in ["sentence_index", "sentence"]
                                ],
                                id="user-dialog",
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
                                    },
                                    {
                                        "if": {"column_id": "sentence"},
                                        "max-width": "45vw",
                                        "min-width": "45vw",
                                    },
                                ],
                                style_header={
                                    "backgroundColor": "rgb(210, 210, 210)",
                                    "color": "black",
                                    "fontWeight": "bold",
                                },
                                page_size=20,
                            ),
                        ),
                    ],
                    className="col-start-3 col-end-7 row-start-1 row-end-7 flex",
                ),
            ],
            className="grid grid-cols-6 grid-rows-6",
        ),
        html.Div(
            [
                html.Div(
                    children=[
                        html.Div("• Raw Data Viewer", className="card-value title"),
                    ],
                    className="col-start-1 col-end-3 row-start-1 row-end-2",
                ),
                html.Div(
                    [
                        dcc.Checklist(
                            options=opts,
                            labelStyle={
                                "display": "flex",
                                "align-items": "center",
                                "font-size": "22px",
                                # "font-weight":"bold"
                                "padding": "10px",
                            },
                            inline=True,
                            style={
                                "flex-wrap": "wrap",
                                "display": "flex",
                                "flex-direction": "row",
                                "padding": "20px",
                            },
                            id="column-list",
                            value=[
                                "sentence_index",
                                "time",
                                "place",
                                "date",
                                "topic",
                                "wday",
                                "goal_topic",
                                "goal_type",
                                "knowledge",
                                "recdial",
                            ],
                        )
                    ],
                    className="col-start-3 col-end-7 row-start-1 row-end-2 flex flex-col fig",
                ),
                html.Div(
                    children=[
                        html.Div(
                            "accepted_food", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-food+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "accepted_movies", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-movies+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "rejected_movies", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-movies-",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "accepted_movie", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-movie+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "accepted_music", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[],
                                    id="user-music1+",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-music2+",
                                ),
                            ],
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "rejected_music", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-music-",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "accepted_celebrity", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-celebrity+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("rejected", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="user-reject",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("poi", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="user-poi",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("accepted_poi", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="user-poi+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("news", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[],
                            id="user-news",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div(
                            "accepted_news", className="col-start-1 col-end-2 p-2"
                        ),
                        html.Div(
                            children=[],
                            id="user-news+",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                    ],
                    className="col-start-1 col-end-3 row-start-2 row-end-7 grid grid-rows-3 grid-cols-2 fig p-4",
                ),
                html.Div(
                    dash_table.DataTable(
                        data=data.df_sentence.to_dict("records"),
                        columns=[
                            {"name": c, "id": c}
                            for c in [
                                "sentence_index",
                                "time",
                                "place",
                                "date",
                                "topic",
                                "wday",
                                "goal_topic",
                                "goal_type",
                                "knowledge",
                                "recdial",
                            ]
                        ],
                        id="raw-data",
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
                    className="col-start-3 col-end-7 row-start-2 row-end-7 p-4",
                ),
            ],
            className="grid grid-cols-6 grid-rows-6",
        ),
        html.Div(
            "Loading...",
            style={
                "padding": "20px",
            },
        ),
    ],
    className="content no-scrollbar flex flex-col",
)
