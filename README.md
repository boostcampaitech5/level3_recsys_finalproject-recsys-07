# DASHMON
대화형 추천시스템의 효과적인 모니터링을 위한 시각화 도구  
<img src = "./images/logo.png" width="80%" height="80%">

## 시연 영상
![record](./images/final.gif)

## 프로젝트 소개

최근 ChatGPT, AskUP 등의 대화형 AI가 각광받으면서 **대화형 추천시스템**(Conversational Recommender System)에 대한 기대와 수요가 높아지고 있습니다.

DashMon은 챗봇으로 대표되는 대화형 추천시스템을 운영할 때,
그 효과와 효율, 품질을 시각화하는 대시보드를 제공하여 시스템 개선을 돕습니다.

대화형 추천시스템을 개발하고 관리하는 매니저들에게
 업로드만으로 사용 가능한 대시보드를 제공하여 시간적, 경제적 자원의 절감을 기대할 수 있습니다.

관리자들은 DashMon을 통해 데이터에 대한 정보를 얻고 LLM 및 추천시스템 모델 개선 여부를 결정하는 데 도움을 얻을 수 있습니다.
> **대화형 추천시스템이란?**\
> 시스템과 사용자 간의 자연어 대화를 통해 사용자의 흥미와 선호를 파악하고 이를 추천에 활용하여 사용자에게 보다 적합한 추천 결과를 제공하는 시스템입니다.  


## 서비스 아키텍쳐
![서비스 아키텍쳐](./images/architecture.png)

## DashMon 웹 페이지 기능
DashMon은 크게 Overview, Instance, Data Analysis, Model Evaluation 페이지로 구성됩니다.
#### 1. Overview 페이지
- 대상 데이터셋의 여러 속성들과 분포등을 확인할 수 있으며, 페이지 중앙에 위치한 Slider를 조정하여 대화 시점에 따른 데이터의 분포를 확인할 수 있습니다.
![Overview](./images/overview1.png)

#### 2. Instance 페이지
- 데이터셋을 직접 확인할 수 있습니다. DuRecDial2.0 데이터셋의 경우 각 대화마다 User Profile 정보가 함께 주어지는데, 해당 내용을 편하게 확인할 수 있도록 유저 정보와 대화 정보를 구분하여 제공합니다.
- 데이터를 확인할 때, 열을 선택할 수 있어 필요한 정보만 확인할 수 있습니다.
![Instance](./images/instance1.png)

#### 3. Data Analysis 페이지
- Overview에서 얻지 못한 심층적인 정보를 얻을 수 있습니다.
- 데이터셋에 포함되는 추천의 효과 및 효율, 대화형 데이터의 사용 품질 등을 막대 그래프와 그래프 자료구조 시각화를 통해 확인할 수 있으며, 사용자 임베딩 시각화를 확인할 수 있습니다.
![Data Analysis](./images/dataanalysis1.png)
![Data Analysis](./images/dataanalysis2.png)
![Data Analysis](./images/dataanalysis3.png)

#### 4. Model Evalution 페이지
- 데이터셋을 CRS모델 학습에 활용했을 때의 정량적인 성능 지표를 확인할 수 있으며, 지표에 따른 모델별 순위를 확인할 수 있습니다.
![Model Evalution](./images/modeleval1.png)
![Model Evalution](./images/modeleval2.png)

## DashMon 사용법
1. DashMon 설치    
    ```
    git clone https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-07.git  
    cd level3_recsys_finalproject-recsys-07  
    ```
   
2. 데이터 다운로드 및 전처리

    **DuRecDial 2.0 (en) 데이터 사용(default)**:

    >https://github.com/liuzeming01/DuRecDial.git 에서 data.zip 다운로드\
    en_train.txt 파일을 /data 폴더로 이동\
    run ```python preprocessing.py```  

    다른 데이터 사용
    >DASHMON 웹 사이트의 README.md 형식으로 데이터 포맷 맞추기\
    >README.md의 Bold는 필수로 포함해야 하는 변수

3. DashMon 실행

    curl 및 poetry 설치:
    ```
    apt install curl -y
    curl -sSL https://install.python-poetry.org | python3 -
    echo 'export PATH="/opt/ml/.local/bin:$PATH"' >> /etc/bash.bashrc
    ```
    가상환경 활성화 및 대시보드 실행:
    ```
    poetry shell
    poetry install
    cd frontend
    python app.py
    ```

## 팀원 구성 및 역할
| [<img src="https://github.com/ji-yunkim.png" width="100px">](https://github.com/ji-yunkim) | [<img src="https://github.com/YirehEum.png" width="100px">](https://github.com/YirehEum) | [<img src="https://github.com/osmin625.png" width="100px">](https://github.com/osmin625) | [<img src="https://github.com/Grievle.png" width="100px">](https://github.com/Grievle) | [<img src="https://github.com/HannahYun.png" width="100px">](https://github.com/HannahYun) |
| :--------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------:
|[김지연](https://github.com/ji-yunkim)|[음이레](https://github.com/YirehEum)|[오승민](https://github.com/osmin625)|[조재오](https://github.com/Grievle)|[윤한나](https://github.com/HannahYun)|
|선행연구분석 <br> UI기획 <br> 평가메트릭 구현|Visualization <br> 성능 메트릭 구현 <br> 감성 분석 <br> Feature Engineering|PM <br> 대시보드 기획 <br> 대시보드 구현 <br> 모델 학습 및 성능 측정|백엔드 <br> 유저 임베딩 구현 <br> 모델 학습 및 성능 측정|Visualization <br> Feature Engineering <br> 모델 학습 및 성능 측정|
