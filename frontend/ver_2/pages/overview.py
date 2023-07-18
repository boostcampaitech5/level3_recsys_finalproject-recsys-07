import dash
from dash import dcc, html
from assets import figure, data

dash.register_page(__name__)

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div("데이터셋 개요", className="title"),
                    ],
                    className="col-start-1 col-end-5",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-clipboard-data round card-icon"),
                        html.Div(data.size, className="card-value"),
                        html.Div("# of instances (rows)"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-people-fill round card-icon"),
                        html.Div(children=[data.user_count], className="card-value"),
                        html.Div("# of users"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(
                            className="bi bi-layout-three-columns round card-icon",
                        ),
                        html.Div(len(data.columns), className="card-value"),
                        html.Div("# of features (columns)"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-chat-left-dots round card-icon"),
                        html.Div(
                            [
                                html.Div(
                                    len(data.df["goal_topic"].unique()),
                                    className="card-value",
                                ),
                                html.Div(
                                    len(data.df["goal_type"].unique()),
                                    className="card-value",
                                ),
                                html.Div("# of topics"),
                                html.Div("# of goal_type"),
                            ],
                            className="grid grid-cols-2 grid-rows-2",
                        ),
                    ],
                    className="figure-card",
                ),
            ],
            className="grid grid-cols-4",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            "상황별 분포(주제, 장소, 요일, 시간)", className="card-value title"
                        ),
                    ],
                    className="col-start-1 col-end-7",
                ),
                html.Div(
                    children=[
                        html.Div(
                            [
                                dcc.Graph(
                                    figure=figure.draw_pie_chart(data.df, "goal_type"),
                                    id="pie-chart",
                                    className="fig",
                                ),
                            ],
                            className="col-start-1 col-end-3 row-start-2 row-end-6",
                        ),
                        html.Div(
                            [
                                dcc.RangeSlider(
                                    0, data.max_si, 1, value=[0, 10], id="si-slider"
                                ),
                                html.Div(id="slider-output"),
                            ],
                            className="col-start-3 col-end-7 row-start-2 row-end-3 fig p-6",
                        ),
                        html.Div(
                            dcc.Graph(
                                figure=figure.draw_bar_chart(data.df, "wday"),
                                className="fig",
                                id="bar-chart",
                            ),
                            className="col-start-3 col-end-7 row-start-3 row-end-7",
                        ),
                        html.Div(
                            dcc.RadioItems(
                                options=[
                                    {
                                        "label": html.Span(
                                            "time", className="p-3 text-lg"
                                        ),
                                        "value": "time",
                                    },
                                    {
                                        "label": html.Span(
                                            "place", className="p-3 text-lg"
                                        ),
                                        "value": "place",
                                    },
                                    {
                                        "label": html.Span(
                                            "date", className="p-3 text-lg"
                                        ),
                                        "value": "date",
                                    },
                                    {
                                        "label": html.Span(
                                            "topic", className="p-3 text-lg"
                                        ),
                                        "value": "topic",
                                    },
                                    {
                                        "label": html.Span(
                                            "wday", className="p-3 text-lg"
                                        ),
                                        "value": "wday",
                                    },
                                    # {
                                    #     "label": html.Span(
                                    #         "sentence_index", className="p-3 text-lg"
                                    #     ),
                                    #     "value": "sentence_index",
                                    # },
                                    # {'label':html.Span('sentence',className='p-3 text-lg'),'value':'sentence'},
                                    # {'label':html.Span('goal_topic',className='p-3 text-lg'),'value':'goal_topic'},
                                    {
                                        "label": html.Span(
                                            "goal_type", className="p-3 text-lg"
                                        ),
                                        "value": "goal_type",
                                    },
                                    # {'label':html.Span('knowledge',className='p-3 text-lg'),'value':'knowledge'},
                                ],
                                value="goal_type",
                                id="column-radio",
                                className="fig p-4 column-radio",
                            ),
                            className="col-start-1 col-end-3 row-start-6 row-end-7",
                        ),
                    ],
                    className="col-start-1 col-end-7 row-start-2 row-end-4 grid-cols-6 grid grid-row-6",
                ),
                html.Div(
                    children=[
                        html.Div(
                            "대화 경과에 따른 의도 분포 / 대화 의도 분포", className="card-value title"
                        ),
                    ],
                    className="col-start-1 col-end-7",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_line_chart(data.df, "goal_type"),
                        className="fig",
                    ),
                    className="col-start-1 col-end-5",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_pie_chart(data.df, "goal_topic"),
                        className="fig",
                    ),
                    className="col-start-5 col-end-7",
                ),
            ],
            className="grid grid-cols-6",
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
