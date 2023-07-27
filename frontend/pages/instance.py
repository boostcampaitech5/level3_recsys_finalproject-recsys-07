import dash
from dash import Input, Output, callback, dash_table, dcc, html
import plotly.graph_objects as go
from assets.data import df_user, df_sentence

dash.register_page(__name__)

opts = [{"label": "sentence_index", "value": "sentence_index", "disabled": True}]
opts.extend(
    [
        {"label": c, "value": c}
        for c in [
            "goal_topic",
            "goal_type",
            "knowledge",
            "recdial",
        ]
    ]
)

layout = html.Div(
    [
        html.Div(  # instance
            [
                html.Div(
                    [
                        html.Div(  # 소제목
                            "사용자 프로필 분포 확인하기",
                            className="title",
                            style={"grid-area": "1 / 1 / span 1 / span 4"},
                        ),
                        dcc.RadioItems(  # 사용자 프로필 column 선택 버튼
                            options=[
                                {
                                    "label": html.Span("나이", className="p-3 text-lg"),
                                    "value": "user_profile_age_range",
                                },
                                {
                                    "label": html.Span("성별", className="p-3 text-lg"),
                                    "value": "user_profile_gender",
                                },
                                {
                                    "label": html.Span("고용상태", className="p-3 text-lg"),
                                    "value": "user_profile_occupation",
                                },
                            ],
                            value="user_profile_gender",
                            id="user-column-radio",
                            className="column-radio",
                            style={"grid-area": "2 / 1 / span 1 / span 4"},
                        ),
                        # 선택 가능한 사용자의 feature --> age_range, gender, occupation
                        dcc.Graph(
                            # figure=figure.draw_user_pie_chart(data.df_user, "user_profile_gender"),
                            id="user-pie-chart",
                            className="fig",
                            style={"grid-area": "3 / 1 / span 6 / span 5"},
                        ),
                        # input
                        html.Div(
                            children=[
                                html.Span("Instance Index : "),
                                dcc.Input(
                                    id="inst-user-id",
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
                        html.Div(  # 유저 프로필
                            [
                                html.Div(
                                    "name",
                                    className="col-start-1 col-end-2 p-2 row-start-1 row-end-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-name",
                                    className="user-info col-start-2 col-end-3 row-start-1 row-end-2",
                                ),
                                html.Div(
                                    "gender",
                                    className="col-start-1 col-end-2 p-2 row-start-2 row-end-3",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-gender",
                                    className="user-info col-start-2 col-end-3 row-start-2 row-end-3",
                                ),
                                html.Div(
                                    "age",
                                    className="col-start-1 col-end-2 p-2 row-start-3 row-end-4",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-age",
                                    className="user-info col-start-2 col-end-3 row-start-3 row-end-4",
                                ),
                                html.Div(
                                    "residence",
                                    className="col-start-3 col-end-4 p-2 row-start-1 row-end-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-residence",
                                    className="user-info col-start-4 col-end-5 row-start-1 row-end-2",
                                ),
                                html.Div(
                                    "occupation",
                                    className="col-start-3 col-end-4 p-2 row-start-2 row-end-3",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-occupation",
                                    className="user-info col-start-4 col-end-5",
                                ),
                            ],
                            className="fig",
                            style={
                                "display": "grid",
                                "grid-area": "10 / 1 / span 4 / span 5",
                                "grid-template-columns": "1fr 2fr 1fr 2fr",
                                "grid-template-rows": "repeat(3, minmax(0, 1fr))",
                                "row-gap": "1rem",
                                "padding": "1rem",
                                "justify-items": "start",
                                "align-items": "center",
                            },
                        ),
                        html.Div(
                            [
                                dash_table.DataTable(
                                    # data=data.df_sentence.to_dict("records"),
                                    columns=[
                                        {"name": "idx", "id": "sentence_index"},
                                        # {"name": "is_user", "id": "is_user"},
                                        {"name": "sentence", "id": "sentence"},
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
                                            "if": {
                                                "filter_query": "{is_user} = 0",
                                                # 'column_id': 'is_user'
                                            },
                                            "backgroundColor": "#e2f0ff",
                                        },
                                        {
                                            "if": {"column_id": "sentence_index"},
                                            "max-width": "2vw",
                                            "min-width": "2vw",
                                        },
                                        {
                                            "if": {"column_id": "is_user"},
                                            "max-width": "3vw",
                                            "min-width": "3vw",
                                        },
                                        {
                                            "if": {"column_id": "sentence"},
                                            "max-width": "38vw",
                                            "min-width": "38vw",
                                        },
                                    ],
                                    style_header={
                                        "backgroundColor": "rgb(210, 210, 210)",
                                        "color": "black",
                                        "fontWeight": "bold",
                                    },
                                    page_size=20,
                                ),
                            ],
                            style={
                                "grid-area": "1 / 6 / span 13 / span 7",
                                "overflow": "overlay",
                            },
                        ),
                        html.Div(  # 유저 프로필 -- 추가 정보
                            [
                                html.Div(
                                    "accepted_food",
                                    className="col-start-1 col-end-2 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-food+",
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "accepted_movie",
                                    className="col-start-3 col-end-4 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-movie+",
                                    className="user-info col-start-4 col-end-5",
                                ),
                                html.Div(
                                    "accepted_movies",
                                    className="col-start-1 col-end-2 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-movies+",
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "rejected_movies",
                                    className="col-start-3 col-end-4 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-movies-",
                                    className="user-info col-start-4 col-end-5",
                                ),
                                html.Div(
                                    "accepted_music",
                                    className="col-start-1 col-end-2 p-2",
                                ),
                                html.Div(
                                    children=[
                                        html.Span(
                                            children=[],
                                            id="user-music1+",
                                        ),
                                        html.Span(
                                            children=[],
                                            id="user-music2+",
                                        ),
                                    ],
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "rejected_music",
                                    className="col-start-3 col-end-4 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-music-",
                                    className="user-info col-start-4 col-end-5",
                                ),
                                html.Div(
                                    "accepted_celebrity",
                                    className="col-start-1 col-end-2 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-celebrity+",
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "rejected", className="col-start-3 col-end-4 p-2"
                                ),
                                html.Div(
                                    children=[],
                                    id="user-reject",
                                    className="user-info col-start-4 col-end-5",
                                ),
                                html.Div("poi", className="col-start-1 col-end-2 p-2"),
                                html.Div(
                                    children=[],
                                    id="user-poi",
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "accepted_poi",
                                    className="col-start-3 col-end-4 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-poi+",
                                    className="user-info col-start-4 col-end-5",
                                ),
                                html.Div("news", className="col-start-1 col-end-2 p-2"),
                                html.Div(
                                    children=[],
                                    id="user-news",
                                    className="user-info col-start-2 col-end-3",
                                ),
                                html.Div(
                                    "accepted_news",
                                    className="col-start-3 col-end-4 p-2",
                                ),
                                html.Div(
                                    children=[],
                                    id="user-news+",
                                    className="user-info col-start-4 col-end-5",
                                ),
                            ],
                            className="fig",
                            style={
                                "display": "grid",
                                "grid-area": "14 / 1 / span 5 / span 12",
                                "grid-template-columns": "1fr 4fr 1fr 4fr",
                                "grid-template-rows": "repeat(6, minmax(0, 1fr))",
                                "row-gap": "2rem",
                                "padding": "2rem",
                                "justify-items": "start",
                                "align-items": "center",
                            },
                        ),
                    ],
                    className="section",
                ),
                html.Div(
                    "• Raw Data Viewer",
                    className="card-value title",
                    style={"grid-area": "19 / 1 / span 2 / span 3"},
                ),
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
                    className="flex flex-wrap flex-row p-4",
                    style={"grid-area": "19 / 4 / span 2 / span 9"},
                    id="column-list",
                    value=[
                        "sentence_index",
                        "goal_topic",
                        "goal_type",
                        "knowledge",
                        "recdial",
                    ],
                ),
                html.Div(
                    [
                        dash_table.DataTable(
                            columns=[
                                {"name": c, "id": c}
                                for c in [
                                    "sentence_index",
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
                    ],
                    style={"grid-area": "21 / 1 / span 17 / span 12"},
                ),
            ],
            className="grid grid-cols-12 grid-rows-36",
            id="instance-grid",
        ),
    ],
    className="content no-scrollbar",
)


@callback(
    Output("raw-data", "columns"),
    Input("column-list", "value"),
)
def get_selected_column(column_list):
    return [{"name": c, "id": c} for c in column_list]


@callback(
    Output("user-dialog", "data"),
    Output("raw-data", "data"),
    Output("user-name", "children"),
    Output("user-gender", "children"),
    Output("user-age", "children"),
    Output("user-residence", "children"),
    Output("user-occupation", "children"),
    Output("user-food+", "children"),
    Output("user-movies+", "children"),
    Output("user-movies-", "children"),
    Output("user-movie+", "children"),
    Output("user-music1+", "children"),
    Output("user-music2+", "children"),
    Output("user-music-", "children"),
    Output("user-celebrity+", "children"),
    Output("user-reject", "children"),
    Output("user-poi+", "children"),
    Output("user-poi", "children"),
    Output("user-news+", "children"),
    Output("user-news", "children"),
    Input("inst-user-id", "value"),
)
def get_user_info(user_id):
    user = df_user[df_user.user_id == user_id]
    sentence = df_sentence[df_sentence.user_id == user_id]
    return (
        sentence.to_dict("records"),
        sentence.to_dict("records"),
        user["user_profile_name"].iloc[0],
        user["user_profile_gender"].iloc[0],
        user["user_profile_age_range"].iloc[0],
        user["user_profile_residence"].iloc[0],
        user["user_profile_occupation"].iloc[0],
        user["user_profile_accepted_food"].iloc[0],
        user["user_profile_accepted_movies"].iloc[0],
        user["user_profile_rejected_movies"].iloc[0],
        user["user_profile_accepted_movie"].iloc[0],
        user["user_profile_accepted_music"].iloc[0],
        user["user_profile_accepted_music.1"].iloc[0],
        user["user_profile_rejected_music"].iloc[0],
        user["user_profile_accepted_celebrities"].iloc[0],
        user["user_profile_reject"].iloc[0],
        user["user_profile_accepted_poi"].iloc[0],
        user["user_profile_poi"].iloc[0],
        user["user_profile_favorite_news"].iloc[0],
        user["user_profile_accepted_news"].iloc[0],
    )


@callback(Output("user-pie-chart", "figure"), Input("user-column-radio", "value"))
def draw_user_pie_chart(column):
    """
    column: 출력 원하는 column명
    """
    df = df_user[column].value_counts().to_frame()
    df.columns = ["count"]

    fig = go.Figure(data=[go.Pie(labels=df.index.to_list(), values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")  # 제목

    # fig.show()
    # age_range, gender, occupation, reject
    return fig
