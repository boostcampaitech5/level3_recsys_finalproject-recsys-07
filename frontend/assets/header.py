from dash import dcc, html, callback, Input, Output, State
import dash
import dash_bootstrap_components as dbc

header = html.Div(
    [
        dbc.Navbar(
            children=[
                html.H1(
                    children=["Select Dataset🗃️ →"],
                    style={
                        "margin-left": "3%",
                        "font-weight": "bold",
                        "font-size": "150%",
                    },
                ),
                dcc.Dropdown(
                    id="header-data-dropdown",
                    value="",
                    className="data-selector",
                    optionHeight=50,
                ),
                html.Div(
                    "관리자님, 반갑습니다.",
                    className="user-text",
                ),
                html.Div(className="bi bi-person-fill round user-icon"),
                dbc.Alert(
                    "데이터셋 업로드 진행 중... 데이터 크기에 따라 업로드 시간이 길어질 수 있습니다.",
                    id="upload-progress-alert",
                    className="alert",
                    color="info",
                    dismissable=True,  # 사용자가 닫을 수 있도록 함
                    is_open=False,  # 알림창 초기 상태는 닫힘
                    duration=7000,  # 알림창이 자동으로 닫히는 지연 시간 (밀리초 단위)
                ),
                dbc.Alert(
                    "데이터셋 업로드 완료! 페이지 상단에서 데이터를 선택해주세요.",
                    id="upload-complete-alert",
                    className="alert",
                    color="success",
                    dismissable=True,  # 사용자가 닫을 수 있도록 함
                    is_open=False,  # 알림창 초기 상태는 닫힘
                    duration=7000,  # 알림창이 자동으로 닫히는 지연 시간 (밀리초 단위)
                ),
                dbc.Alert(
                    id="preprocessing-alert",
                    className="alert-2",
                    color="light",
                    dismissable=False,  # 사용자가 닫을 수 있도록 함
                    is_open=False,  # 알림창 초기 상태는 닫힘
                    # duration=7000,  # 알림창이 자동으로 닫히는 지연 시간 (밀리초 단위)
                ),
            ],
            className="header",
            id="header",
        )
    ]
)


@callback(
    Output("header-data-dropdown", "options"),
    Output("upload-complete-alert", "is_open"),
    Input("filename-store", "modified_timestamp"),
    State("filename-store", "data"),
)
def get_filename(ts, filename):
    if ts is None:
        raise dash.exceptions.PreventUpdate
    return [{"label": filename, "value": filename}], True


@callback(
    [
        Output("upload-dataset-text", "style"),
        Output("page0", "style"),
        Output("upload-data", "style"),
        Output("page1", "style"),
        Output("page2", "style"),
        Output("page3", "style"),
        Output("page4", "style"),
    ],
    Input("header-data-dropdown", "value"),
)
def sidebar_btn_show(value):
    if value == "":
        raise dash.exceptions.PreventUpdate
    else:
        return [
            {"display": "none"},
            {"display": "none"},
            {"display": "none"},
            {"visibility": "visible"},
            {"visibility": "visible"},
            {"visibility": "visible"},
            {"visibility": "visible"},
        ]
