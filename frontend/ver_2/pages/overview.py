import dash
import pandas as pd
from dash import html, dcc
from assets import figure

dash.register_page(__name__)

df = pd.read_csv("../../data/durecdial/dev_pp.csv")
layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(className="bi bi-clipboard-data round card-icon"),
                        html.Div(df.size, className="card-value"),
                        html.Div("# of instances (rows)"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-people-fill round card-icon"),
                        html.Div(children=[df.size], className="card-value"),
                        html.Div("# of users"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(
                            className="bi bi-layout-three-columns round card-icon",
                        ),
                        html.Div(len(df.columns), className="card-value"),
                        html.Div("# of features (columns)"),
                    ],
                    className="figure-card",
                ),
                html.Div(
                    children=[
                        html.Div(className="bi bi-chat-left-dots round card-icon"),
                        html.Div("# of topics"),
                        html.Div(len(df["goal_topic"].unique())),
                        html.Div("# of goal_type"),
                        html.Div(len(df["goal_type"].unique())),
                    ],
                    className="figure-card",
                ),
            ],
            className="grid grid-cols-4",
        ),
        html.Div(
            children=[
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_line_chart(df, "goal_type"),
                        className="fig",
                    ),
                    className="col-start-1 col-end-5",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_pie_chart(df, "goal_topic"),
                        className="fig",
                    ),
                    className="col-start-5 col-end-7",
                ),
                html.Div(
                    className="col-start-1 col-end-2 fig",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_pie_chart(df, "goal_type"),
                        className="fig",
                    ),
                    className="col-start-2 col-end-4",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_bar_chart(df, "wday"),
                        className="fig",
                    ),
                    className="col-start-4 col-end-7",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_pie_chart(df, "place"),
                        className="fig",
                    ),
                    className="col-start-1 col-end-3",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_pie_chart(df, "topic"),
                        className="fig",
                    ),
                    className="col-start-3 col-end-5",
                ),
                html.Div(
                    dcc.Graph(
                        figure=figure.draw_bar_chart(df, "time", horizontal=True),
                        className="fig",
                    ),
                    className="col-start-5 col-end-7",
                ),
            ],
            className="grid grid-cols-6 grid-rows-6",
        ),
    ],
    className="content no-scrollbar flex flex-col",
)
