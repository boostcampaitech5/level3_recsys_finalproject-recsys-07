from dash import Input, Output, State, callback, dcc, html
import dash
import dash_bootstrap_components as dbc
import io
import pandas as pd
import numpy as np

sidebar_show = [
    dbc.Nav(
        [
            html.Div(
                [
                    dbc.Button(
                        className="bi bi-list 2px btn-sidebar",
                        id="btn-sidebar",
                    ),
                    dbc.Button(
                        children="DASHMON",
                        className="btn-title",
                        href="/",
                    ),
                ],
                id="header-side-box",
                className="side-header",
            ),
            html.H1(
                children=["Upload Dataset🗃️"],
                # style={"margin-left": "10%", "margin-bottom": "5%"},
                className="side-nav",
                id="upload-dataset-text",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-info-circle side-nav-icon",
                    ),
                    html.Span("README"),
                ],
                href="/readme",
                id="page0",
                active="exact",
                className="side-nav",
            ),
            dcc.Upload(
                children=html.Div("Drag & Drop or Select File"),
                id="upload-data",
                className="upload-btn",
            ),
            dcc.Store(
                id="filename-store",
            ),
            dcc.Store(
                id="date-store",
            ),
            dcc.Store(
                id="data-store",
            ),
            dcc.Store(
                id="pp-data-store",
            ),
            html.Ul(id="file-list"),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door side-nav-icon",
                    ),
                    html.Span("OVERVIEW"),
                ],
                href="/overview",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page1",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-layout-three-columns side-nav-icon",
                    ),
                    html.Span("INSTANCE"),
                ],
                href="/instance",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page2",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-columns side-nav-icon",
                    ),
                    html.Span("DATA ANALYSIS"),
                ],
                href="/dataanalysis",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page3",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-cpu side-nav-icon",
                    ),
                    html.Span("MODEL EVALUATION"),
                ],
                href="/modelevaluation",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page4",
            ),
        ],
        vertical=True,
        pills=True,
    ),
]

sidebar_hidden = [
    dbc.Nav(
        [
            dbc.Button(
                className="bi bi-list 2px btn-sidebar",
                id="btn-sidebar",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-house-door side-nav-icon",
                    )
                ],
                href="/overview",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page1",
            ),
            dbc.NavLink(
                [
                    html.Span(
                        className="bi bi-layout-three-columns side-nav-icon",
                    )
                ],
                href="/instance",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page2",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-columns side-nav-icon")],
                href="/dataanalysis",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page3",
            ),
            dbc.NavLink(
                [html.Span(className="bi bi-cpu side-nav-icon")],
                href="/modelevaluation",
                active="exact",
                className="side-nav",
                style={
                    "visibility": "hidden",
                },
                id="page4",
            ),
        ],
        vertical=True,
        pills=False,
    ),
]

sidebar = html.Div(
    children=sidebar_show,
    className="sidebar side-show",
    id="sidebar",
)


@callback(
    [
        Output("header", "className"),
        Output("sidebar", "className"),
        Output("sidebar", "children"),
        Output("page_content", "className"),
        Output("side_click", "data"),
    ],
    [Input("btn-sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ],
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            header_className = "header content-side-hidden"
            sidebar_className = "sidebar side-hidden"
            sidebar_children = sidebar_hidden
            content_className = "content content-side-hidden"
            cur_nclick = "HIDDEN"
        else:
            header_className = "header content-side-show"
            sidebar_className = "sidebar side-show"
            sidebar_children = sidebar_show
            content_className = "content content-side-show"
            cur_nclick = "SHOW"
    else:
        header_className = "header content-side-show"
        sidebar_className = "sidebar side-show"
        sidebar_children = sidebar_show
        content_className = "content content-side-show"
        cur_nclick = "SHOW"

    return (
        header_className,
        sidebar_className,
        sidebar_children,
        content_className,
        cur_nclick,
    )


@callback(
    Output("filename-store", "data"),
    Output("date-store", "data"),
    Output("data-store", "data"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def update_data_store(content_string, filename, date):
    if content_string is not None:
        print("uploaded file: ", filename)
        try:
            if "csv" in filename:
                df = pd.read_csv(io.StringIO(content_string))
                print("csv 데이터파일 읽는 중...")
            elif "xls" in filename:
                df = pd.read_excel(io.BytesIO(content_string))
        except Exception as e:
            print(e)
            return "There was an error processing this file.", None, None
        return filename, date, df.to_dict("records")
    if content_string is None:
        raise dash.exceptions.PreventUpdate


@callback(
    Output("pp-data-store", "data"),
    Input("data-store", "modified_timestamp"),
    State("data-store", "data"),
    State("date-store", "data"),
)
def data_preprocessing(ts, df_dict, date):
    # ts : 무시하면 됨.
    # 데이터가 저장된 store 객체의 data 파일을
    # callback 함수에서 Input으로 바로 불러올 수 없기 때문에
    # 우회하기 위해 Store의 파라미터 modified_timestamp를 호출하는 것.
    # ---
    # df_dict : to_dict('record')가 적용된 df. 즉, dict 타입.
    # ---
    # date : 무시하면 됨. 데이터가 업로드된 시점을 의미하는 변수.
    if ts is None:
        raise dash.exceptions.PreventUpdate

    # frontend에 데이터를 업로드 하면 파생변수를 생성하는 전처리 수행하는 코드
    """
    index: 모든 대화의 순서(임의: 데이터의 행 번호)
    recdial: 추천 대화인지 여부(1: 추천 관련 대화, 0: 추천 관련 없는 대화)
    is_bot_talk_first: 대화에서 봇이 먼저 시작했는지 여부(1: 봇이 대화 시작, 0: 사람이 대화 시작) // Greetings(goal_type) 존재해야 함
    is_user: 해당 문장이 봇의 대화 인지, 사용자의 대화인지 구분(1: 사람, 0: 봇)
    # TODO: 변수 설명 작성
    sentiment_star: 
    sentiment_score: 
    deny: 사용자의 추천을 거절했는 지 여부(TRUE: 추천 거절, FALSE: 추천 받아들임)
    recommend_sf: 추천의 성공 여부(Success: 추천 성공, Failure: 추천 실패)
    """

    # dict 타입의 df_dict를 dataframe으로 변환
    df = pd.DataFrame.from_dict(data=df_dict, orient='columns')

    # recdial 변수 생성
    df['recdial'] = np.where(df['goal_type'].str.contains('recommendation'), 1, 0)

    # idx 0번째에는 sentence, idx 1번째에는 goal_type
    # user_id번째의 index에 두가지 정보가 저장되어 있음
    # first_start_list[example_user_id][0 or 1] 과 같이 사용가능
    first_start_list = []
    user_list = []

    for idx in range(len(df)):
        if df['user_id'].iloc[idx] not in user_list:
            first_start_list.append([df['sentence'].iloc[idx], df['goal_type'].iloc[idx]])
            user_list.append(df['user_id'].iloc[idx])
                
    # is_bot_talk_first 변수 생성 // Greetings(goal_type) 존재해야 함
    data = []
    for idx in range(len(df)):
        if first_start_list[df.iloc[idx]['user_id']][1] == 'Greetings':
            data.append(1)
        else:
            data.append(0)

    df['is_bot_talk_first'] = data
        
    # is_user 변수 생성
    is_user = []
    for idx in range(len(df)):
        if df.iloc[idx]['is_bot_talk_first'] == 0: # 유저가 먼저 대화 시작
            if df.iloc[idx]['sentence_index'] % 2 == 0:
                is_user.append(1) # 유저
            else:
                is_user.append(0) # 봇
        else: # 봇이 먼저 대화 시작
            if df.iloc[idx]['sentence_index'] % 2 == 0:
                is_user.append(0) # 봇
            else:
                is_user.append(1) # 유저

    df['is_user'] = is_user

    # TODO: 감성 분석


    # recommend_sf 변수 생성
    data = []
    for idx in range(len(df)):
        if df.iloc[idx]['recdial'] == 1:
            if idx != 0 and df.iloc[idx-1]['recdial'] == 0 and df.iloc[idx]['is_user'] == 1:
                data.append(np.nan)
                continue
            if df.iloc[idx]['is_user'] == 1 and df.iloc[idx]['deny']==False:
                data.append("Success")
            elif df.iloc[idx]['is_user'] == 1 and df.iloc[idx]['deny']==True:
                data.append("Failure")
            else:
                data.append(np.nan)
        else:
            data.append(np.nan)

    df['recommend_sf'] = data

    # index 변수 생성
    data = []
    for idx in range(1, len(df)+1):
        data.append(idx)

    df['index'] = data
    
    # 데이터프레임 열 순서 변경 -> index가 맨 앞으로
    col1 = df.columns[:-1].to_list()
    col2 = df.columns[-1:].to_list()
    new_col = col2 + col1
    df = df[new_col]
    
    df_pp = df
    # df_pp = pd.DataFrame()
    return df_pp.to_dict("records")  # 전처리가 완료된 데이터셋


@callback(
    Output("upload-progress-alert", "is_open"),
    Input("upload-data", "filename"),
)
def update_progress_alert(filename):
    if filename:
        return True
