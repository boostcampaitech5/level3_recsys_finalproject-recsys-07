import plotly.express as px
import plotly.graph_objects as go


def draw_pie_chart(df, column, min_range=0, max_range=50):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
    """
    df = (
        df[[column]]
        .loc[(df["sentence_index"] >= min_range) & (df["sentence_index"] <= max_range)]
        .value_counts()
        .to_frame()
    )
    df.columns = ["count"]
    df.reset_index(inplace=True)
    if df.shape[0] > 10:
        df.loc[9] = ["기타", df["count"].iloc[10:].sum()]
        df = df.iloc[:10]
    fig = go.Figure(data=[go.Pie(labels=df[column], values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )  # figure에서는 테두리를 둥글게 만들 수 없어서 배경색을 투명하게 설정.
    # fig.show()
    return fig


def draw_bar_chart(df, column, min_range=0, max_range=50, horizontal=False):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
    horizontal : 가로 출력 여부
    """
    df = df[column].value_counts().to_frame().reset_index()
    df.columns = [column, "count"]
    if horizontal:
        fig = px.bar(df, x="count", y=column, orientation="h")
    else:
        fig = px.bar(df, x=column, y="count")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)"
    )  # figure에서는 테두리를 둥글게 만들 수 없어서 배경색을 투명하게 설정.
    return fig


def draw_line_chart(dataframe, column, min_range=0, max_range=50, smooth=True):
    """
    column : 출력 원하는 column명
    min_range, max_range : 함수에 표시할 sentence_index 범위, 기본값 [0, 50]
    smooth : 그래프 부드럽게 그리는 여부
    """
    if smooth:
        shape = "spline"
    else:
        shape = "linear"
    df = dataframe[[column, "sentence_index"]].value_counts().to_frame()
    df.columns = ["count"]
    df.reset_index(inplace=True)
    df.sort_values(by=[column, "sentence_index"], inplace=True)
    fig = px.line(
        df, x="sentence_index", y="count", color="goal_type", line_shape=shape
    )
    # fig.show()
    return fig


def draw_gender_pie_chart(df, column):
    """
    column: 출력 원하는 column명
    """
    df = df[column].value_counts().to_frame()
    df.columns = ["count"]

    fig = go.Figure(data=[go.Pie(labels=df.index.to_list(), values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")  # 제목

    # fig.show()
    return fig


def draw_gender_bar_chart(df, column, gender="", range=5, horizontal=False):
    """
    column : 출력 원하는 column명
    gender : 성별 (default= '', Female, Male)
    range : 몇 개까지 출력할 것인지 범위
    horizontal : 가로 출력 여부
    """
    if gender != "":
        df = df[df["user_profile_gender"] == f"{gender}"]
        df = df[column].value_counts().to_frame()
    else:
        df = df[column].value_counts().to_frame()
    df = df[:range]
    df.columns = ["count"]

    lab = df.index.to_list()[:range]

    if horizontal:
        fig = px.bar(df, x="count", y=lab, orientation="h", text_auto=True)
    else:
        fig = px.bar(df, x=lab, y="count", text_auto=True)
    # fig.show()
    return fig
