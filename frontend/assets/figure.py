import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from assets.perflexity import d_pp
from assets.ngram import d_array


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


def perflexity():
    group_labels = ["Dialogue Perplexity"]  # name of the dataset

    fig = ff.create_distplot([d_pp], group_labels, bin_size=0.1)
    fig.update_layout(
        autosize=True,
        # width=800,
        # height=800,
        xaxis=dict(
            title_text="Dialogue Count",
        ),
        yaxis=dict(title_text="Perplexity"),
        title_text=f"Distribution of Dialogue Perplexity (n=2) <br><br> <sup>Average perplexity of the dataset : \
            {round(sum(d_pp)/len(d_pp),4)}</sup>",
    )
    fig.update_yaxes(automargin=True)
    fig.update_xaxes(automargin=True)
    return fig


def ngram():
    group_labels = ["Distinct N-gram"]  # name of the dataset

    fig = ff.create_distplot([d_array], group_labels, bin_size=0.005)
    fig.update_layout(
        autosize=True,
        # width=800,
        # height=800,
        yaxis=dict(
            title_text="Dialogue Count",
        ),
        title_text="Distribution of Dialogue-level Distinct N-gram",
    )
    fig.update_yaxes(automargin=True)
    return fig
