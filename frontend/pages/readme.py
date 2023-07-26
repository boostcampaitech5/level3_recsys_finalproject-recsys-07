import dash
from dash import html
from dash import dash_table
import pandas as pd

dash.register_page(__name__)

df = pd.DataFrame(
    [
        ["user_id", "integer", "각 사용자의 고유번호", "0"],
        ["user_profile_age_range", "String", "사용자의 연령대 (임의설정 가능)", "Over 50 years old"],
        ["user_profile_name", "String", "사용자의 이름 (암호화 가능)", "Fangyang Liu"],
        ["user_profile_residence", "String", "사용자의 거주지", "Qingdao"],
        [
            "user_profile_accepted_food",
            "String",
            "사용자의 선호 음식",
            "Ziaoji stuffed with mackerel",
        ],
        [
            "user_profile_accepted_movies",
            "List of String",
            "사용자의 선호 영화",
            "['Left Right Love Destiny', 'Hot Summer Days', 'Fly Me to Polaris', \
                'Help!!!', 'One Night in Mongkok', 'The Bullet Vanishes']",
        ],
        ["user_profile_accepted_music", "List of String", "사용자의 선호 음악", "['Once']"],
        ["user_profile_rejected_music", "List of String", "사용자의 불호 음악", "['Its Time']"],
        ["user_profile_gender", "String", "사용자의 성별", "Female"],
        [
            "user_profile_accepted_celebrities",
            "List of String",
            "사용자의 선호 유명인",
            "['Cecilia Cheung', 'Kris Wu', 'Nicholas Tse']",
        ],
        ["user_profile_accepted_movie", "String", "사용자의 선호 영화", "The Legend of Speed"],
        ["user_profile_reject", "String", "사용자의 불호 매체", "News"],
        [
            "user_profile_rejected_movies",
            "List of String",
            "사용자의 불호 영화",
            "['Everyday is Valentine', 'Unforgettable', 'King of Comedy']",
        ],
        ["user_profile_occupation", "String", "사용자의 직업 및 고용상태", "Student"],
        [
            "user_profile_accepted_poi",
            "String",
            "사용자가 선호 관심 지점",
            "Minguo Seafood Dumpling House",
        ],
        [
            "user_profile_favorite_news",
            "List of String",
            "사용자가 가장 선호하는 뉴스기사",
            "['Jacky Cheungs news']",
        ],
        [
            "user_profile_accepted_news",
            "List of String",
            "사용자의 선호 뉴스",
            "['Leslie Cheungs news, Leehom Wangs news']",
        ],
        [
            "user_profile_poi",
            "String",
            "사용자가 밝힌 관심 지점",
            "Mingyuan Spicy Hot Pot-Chongqing Roasted Fish",
        ],
        ["time", "time", "발화가 이루어진 시각", "12:00:00 PM"],
        ["place", "String", "발화가 이루어진 장소", "at school"],
        ["date", "date", "발화가 이루어진 날짜", "2018-10-19"],
        ["topic", "String", "발화의 상황 주제", "Academic setback"],
        ["wday", "String", "발화가 이루어진 요일", "Wednesday"],
        ["sentence_index", "integer", "한 대화 내 발화의 순번", "0"],
        [
            "sentence",
            "String",
            "발화 문장의 내용",
            "Who is the leading actor of the movie Left Right Love Destiny?",
        ],
        ["goal_topic", "String", "발화 목적 키워드", "Cecilia Cheung"],
        ["goal_type", "String", "발화 목적", "Chat about stars"],
        [
            "knowledge",
            "String",
            "발화에 쓰인 배경지식 키워드",
            "Cecilia Cheung, Stars, Left Right Love Destiny",
        ],
    ],
    columns=["열 이름", "데이터 타입", "설명", "예시"],
)


layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3(
                    children="📤 로그 데이터 업로드",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        "DashMon에 대화형 추천시스템의 로그데이터를 업로드하여 정량적, 정성적으로 분석할 수 있습니다.",
                        html.Br(),
                        "DashMon을 효과적으로 이용하기 위해 아래와 같은 포맷을 지켜 업로드해주세요.",
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
                html.H3(
                    children="📤 Dataset Format",
                    style={
                        "font-weight": "bold",
                        "font-size": "150%",
                        "line-height": "200%",
                        "margin-top": "3%",
                    },
                ),
                html.H4(
                    children=[
                        html.A(
                            "예시 데이터셋 : DuRecDial2.0(EN)",
                            # href="../../data/durecdial/sample_data.csv",
                            className="text-lg font-bold",
                        ),
                        html.Br(),
                        " 데이터셋의 Feature(column)와 data type은 다음과 같습니다.",
                        dash_table.DataTable(
                            id="table",
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict("records"),
                            # export_format="csv",
                            style_table={"width": "80%"},
                            style_header={"font-weight": "bold"},
                            style_cell={"textAlign": "left"},
                        ),
                    ],
                    style={"margin-left": "5%", "line-height": "200%"},
                ),
            ],
        ),
        html.Div(className="p-8"),
    ],
    style={
        "display": "flex",
        "flex-direction": "column",
        "height": "93vh",
        "overflow": "scroll",
    },
    className="no-scrollbar",
)
