import dash
import pandas as pd
from dash import html, dcc
from assets import css
from assets import figure

dash.register_page(__name__, path="/")

# the style arguments for the sidebar. We use position:fixed and a fixed width

# the styles for the main content position it to the right of the sidebar and
# add some padding.

df = pd.read_csv("../../data/durecdial/dev_pp.csv")

content = html.Div(
    [
        html.Div(
            "Overview",
            style={
                "font-size": "2vw",
                "font-weight": "bold",
            },
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            "Goal Distribution",
                            style={
                                "font-size": "1.5vw",
                                "font-weight": "bold",
                            },
                        ),
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
                        "min-width": "40%",
                        "min-height": "100%",
                    },
                ),
                html.Div(
                    children=[
                        html.Div(
                            "Situation Distribution",
                            style={
                                "font-size": "1.5vw",
                                "font-weight": "bold",
                            },
                        ),
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
                                "display": "flex",
                                "display-direction": "row",
                                "min-width": "100%",
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
                        "min-width": "60%",
                        "min-height": "100%",
                    },
                ),
            ],
            style={
                "display": "flex",
                "display-direction": "row",
                # 'min-width':'100%',
            },
        ),
    ],
    id="page-content",
)

layout = html.Div(
    children=[
        content,
    ],
)
