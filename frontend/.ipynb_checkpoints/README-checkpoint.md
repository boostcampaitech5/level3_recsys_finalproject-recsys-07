apt install curl -y
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/opt/ml/.local/bin:$PATH"' >> /etc/bash.bashrc

poetry shell  ==> 가상환경 활성화
poetry install ==> 기록된 패키지 설치
frontend/ver_2/ 경로로 이동
python app.py  ==> 대시보드 실행