import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        html.Img(src='../assets/images/dashmon-high-resolution-color-logo.png', style={'max-width':'20%'}),
        html.H1(children='Welcome to DASHMON!📊', className='blink', style={'font-weight':'bold','margin-top':'3%','line-height':'150%','font-size':'200%'}),
        html.H2('DASHMON은 대화형 추천시스템에서 활용되는 데이터를 시각화하고 분석하는 모니터링 툴입니다.',style={'line-height':'200%'}),
        html.Div(
            children=[
                html.H3(children='💡 DASHMON의 목표',style={'font-weight':'bold','font-size':'150%','line-height':'200%','margin-top':'3%'}),
                html.H4(children='DASHMON은 Conversational Recommender System(CRS)을 개발하고 유지하는 데에 ',style={'margin-left':'5%','line-height':'200%'}),
                html.H3(children='💡 DASHMON의 기능',style={'font-weight':'bold','font-size':'150%','line-height':'200%','margin-top':'3%'}),
                html.H4(children='DASHMON은 ',style={'margin-left':'5%','line-height':'200%'})
            ]
        ),
    ]
)
