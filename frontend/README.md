apt install curl -y
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="/opt/ml/.local/bin:$PATH"' >> /etc/bash.bashrc
poetry init
poetry shell  ==> 가상환경 활성화