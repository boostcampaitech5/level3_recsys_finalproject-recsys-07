import dash
import pandas as pd
from dash import html, dcc
from assets import figure


dash.register_page(__name__)

df = pd.read_csv("../../data/durecdial/dev_pp.csv")
layout = html.Div(
    [
        html.Div(
            children=[
                html.Span(
                    children=[
                        html.Div(className="bi bi-clipboard-data round card-icon"),
                        html.Div(df.size, className="card-value"),
                        html.Div("# of instances (rows)"),
                    ],
                    className="figure-card",
                ),
                html.Span(
                    children=[
                        html.Div(className="bi bi-people-fill round card-icon"),
                        html.Div(children=[df.size], className="card-value"),
                        html.Div("# of users"),
                    ],
                    className="figure-card",
                ),
                html.Span(
                    children=[
                        html.Div(
                            className="bi bi-layout-three-columns round card-icon",
                        ),
                        html.Div(len(df.columns), className="card-value"),
                        html.Div("# of features (columns)"),
                    ],
                    className="figure-card",
                ),
                html.Span(
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
            style={
                "min-height": "22vh",
                "display": "flex",
                "justify-content": "space-around",
            },
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=figure.draw_pie_chart(df, "goal_type"),
                            className="fig",
                        ),
                        dcc.Graph(
                            figure=figure.draw_pie_chart(df, "goal_topic"),
                            className="fig",
                        ),
                    ],
                    style={
                        "width": "40%",
                        "height": "100%",
                    },
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=figure.draw_bar_chart(df, "wday"),
                            className="fig",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    figure=figure.draw_pie_chart(df, "place"),
                                    className="fig",
                                ),
                                dcc.Graph(
                                    figure=figure.draw_pie_chart(df, "topic"),
                                    className="fig",
                                ),
                            ],
                            style={
                                # "display": "flex",
                                # "display-direction": "row",
                                # "min-width": "100%",
                                # 'min-heigh':'100%',
                            },
                        ),
                        dcc.Graph(
                            figure=figure.draw_bar_chart(df, "time"),
                            className="fig",
                        ),
                    ],
                    style={
                        # 'display':'flex',
                        # 'display-direction':'column',
                        # 'flex-wrap':'wrap',
                        # "min-width": "60%",
                        # "min-height": "100%",
                    },
                ),
            ],
            style={
                # "display": "flex",
                # 'flex-wrap':'wrap',
                # "min-width": "100%",
                # "min-height": "100%",
                # "display-direction": "row",
                # 'min-width':'100%',
            },
        ),
    ],
)
