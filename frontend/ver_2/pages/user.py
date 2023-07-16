import dash
from dash import html, dcc, dash_table
from assets import data

dash.register_page(__name__)

layout = html.Div(
    children=[
        html.Div(
            children=[
                # html.Div(
                #     children=[
                #         html.Div(
                #             dcc.RadioItems(
                #                 options=[
                #                     {
                #                         "label": html.Span(
                #                             "male", className="p-3 text-lg"
                #                         ),
                #                         "value": "male",
                #                     },
                #                     {
                #                         "label": html.Span(
                #                             "female", className="p-3 text-lg"
                #                         ),
                #                         "value": "female",
                #                     },
                #                 ],
                #                 value="male",
                #                 id="column-radio",
                #                 className="fig p-4 flex flex-auto flex-row",
                #             ),
                #             className="row-start-1 row-end-2",
                #         ),
                #         html.Div(
                #         children=[
                #             html.Div(data.size, className="card-value"),
                #             html.Div("% of male"),
                #         ],
                #         className="figure-card",
                # ),
                #     ],
                #     className="col-start-1 col-end-3 grid-rows-2",
                # ),
                html.Div(
                    children=[
                        dcc.Input(
                            id="user-id",
                            type="number",
                            placeholder="Search user-ID",
                            value=5,
                        )
                    ],
                    className="col-start-1 col-end-3 row-start-1 row-end-2 p-4 fig",
                ),
                html.Div(
                    # name gender age residence occupation place
                    children=[
                        html.Div("name", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[data.user_count],
                            id="user-name",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("gender", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[data.user_count],
                            id="user-gender",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("age", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[data.user_count],
                            id="user-age",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("residence", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[data.user_count],
                            id="user-residence",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                        html.Div("occupation", className="col-start-1 col-end-2 p-2"),
                        html.Div(
                            children=[data.user_count],
                            id="user-occupation",
                            className="user-info col-start-2 col-end-3 p-2",
                        ),
                    ],
                    className="col-start-1 col-end-3 row-start-2 row-end-4 grid grid-rows-3 grid-cols-2 fig p-4",
                ),
                html.Div(
                    children=[
                        html.Div(
                            dash_table.DataTable(
                                data=data.df.to_dict("records"),
                                columns=[{"name": "sentence", "id": "sentence"}],
                                id="user-dialog",
                                style_cell={
                                    "textAlign": "left",
                                    "padding": "10px 0px 10px 30px",
                                },
                                style_as_list_view=True,
                                style_data={
                                    "color": "black",
                                    "backgroundColor": "white",
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
                                page_size=20,
                            ),
                        ),
                    ],
                    className="fig col-start-3 col-end-7 row-start-1 row-end-7",
                ),
                # html.Div(
                #     dcc.Graph(
                #         figure=figure.draw_gender_bar_chart(data.df, "goal_topic",'',10,True),
                #         className="fig",
                #     ),
                #     className="col-start-3 col-end-7",
                # ),
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
