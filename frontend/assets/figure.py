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
        df,
        x="sentence_index",
        y="count",
        color="goal_type",
        line_shape=shape,
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    # fig.show()
    return fig


def draw_user_pie_chart(df, column):
    """
    column: 출력 원하는 column명
    """
    df = df[column].value_counts().to_frame()
    df.columns = ["count"]

    fig = go.Figure(data=[go.Pie(labels=df.index.to_list(), values=df["count"])])
    fig.update_traces(textinfo="percent")
    fig.update_layout(title=f"{column} Distribution")  # 제목

    # fig.show()
    # age_range, gender, occupation, reject
    return fig


def draw_user_bar_chart(df, column, gender="", range=5, horizontal=False):
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
        fig = px.bar(
            df,
            x="count",
            y=lab,
            orientation="h",
            text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Set1,
        )
    else:
        fig = px.bar(
            df,
            x=lab,
            y="count",
            text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Set1,
        )
    # fig.show()
    return fig

def draw_recommend_sf_chart(df, column):
    """
    column : 출력 원하는 column명
    """
    # 라벨
    top_labels = ['Success', 'Failure']

    # 차트 색깔
    colors = [px.colors.qualitative.Plotly, px.colors.qualitative.Plotly[1]]

    # 데이터
    value_counts = df[column].value_counts()
    total_count = value_counts.sum()
    df_percentage = (value_counts / total_count * 100)
    x_data = [[df_percentage[0].round(1), df_percentage[1].round(1)]]

    # id값(아직 보이게 설정안함)
    y_data = ['success_failure Distribution']

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                    color=colors[i],
                    line=dict(color='rgb(248, 248, 249)', width=1)
                )
            ))

    fig.update_layout(
        title=dict(
            text = f'{y_data[0]}',
            font = dict(size=36),
            x = 0.5,
            pad=dict(b=1000, t=1000),
        ),
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        showlegend=False,
        margin=dict(t=140, b=80),
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=20,
                                        color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=20,
                                        color='rgb(67, 67, 67)'),
                                showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
                # labeling the rest of percentages for each bar (x_axis)
                annotations.append(dict(xref='x', yref='y',
                                        x=space + (xd[i]/2), y=yd,
                                        text=str(xd[i]) + '%',
                                        font=dict(family='Arial', size=20,
                                                color='rgb(248, 248, 255)'),
                                        showarrow=False))
                # labeling the Likert scale
                if yd == y_data[-1]:
                    annotations.append(dict(xref='x', yref='paper',
                                            x=space + (xd[i]/2), y=1.1,
                                            text=top_labels[i],
                                            font=dict(family='Arial', size=20,
                                                    color='rgb(67, 67, 67)'),
                                            showarrow=False))
                space += xd[i]

    fig.update_layout(annotations=annotations)
    # fig.show()
    return fig
    