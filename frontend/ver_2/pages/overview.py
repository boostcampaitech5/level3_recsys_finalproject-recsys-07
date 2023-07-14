import dash
import pandas as pd
from dash import html, dcc
from assets import css
from assets import figure


dash.register_page(__name__)

# the style arguments for the sidebar. We use position:fixed and a fixed width

# the styles for the main content position it to the right of the sidebar and
# add some padding.

df = pd.read_csv("../../data/durecdial/dev_pp.csv")
# print(df.columns)
layout = html.Div(
    [
        html.Div(
            style={
                "height": "7vh",
            }
        ),
        html.Div(
            children=[
                html.Span(
                    children=[
                        html.Div(
                            className="bi bi-clipboard-data round", style=css.CARD_ICON
                        ),
                        html.Div(df.size, style=css.CARD_VALUE),
                        html.Div("# of instances (rows)"),
                    ],
                    style=css.FIGURE_CARD,
                ),
                html.Span(
                    children=[
                        html.Div(
                            className="bi bi-people-fill round", style=css.CARD_ICON
                        ),
                        html.Div(children=[df.size], style=css.CARD_VALUE),
                        html.Div("# of users"),
                    ],
                    style=css.FIGURE_CARD,
                ),
                html.Span(
                    children=[
                        html.Div(
                            className="bi bi-layout-three-columns round",
                            style=css.CARD_ICON,
                        ),
                        html.Div(len(df.columns), style=css.CARD_VALUE),
                        html.Div("# of features (columns)"),
                    ],
                    style=css.FIGURE_CARD,
                ),
                html.Span(
                    children=[
                        html.Div(
                            className="bi bi-chat-left-dots round", style=css.CARD_ICON
                        ),
                        html.Div("# of topics"),
                        html.Div(len(df["goal_topic"].unique())),
                        html.Div("# of goal_type"),
                        html.Div(len(df["goal_type"].unique())),
                    ],
                    style=css.FIGURE_CARD,
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
                            style=css.FIG_STYLE_1,
                        ),
                        dcc.Graph(
                            figure=figure.draw_pie_chart(df, "goal_topic"),
                            style=css.FIG_STYLE_1,
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
                            style=css.FIG_STYLE_2,
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    figure=figure.draw_pie_chart(df, "place"),
                                    style=css.FIG_STYLE_3,
                                ),
                                dcc.Graph(
                                    figure=figure.draw_pie_chart(df, "topic"),
                                    style=css.FIG_STYLE_3,
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
                            style=css.FIG_STYLE_2,
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
