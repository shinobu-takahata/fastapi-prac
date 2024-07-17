# 依存関係をインストールするステージ
FROM python:3.11 as requirements-stage

# 作業ディレクトリを設定
WORKDIR /tmp

# Poetryをインストール
RUN pip install poetry

# 依存関係ファイルをコピー
COPY pyproject.toml poetry.lock* /tmp/

# 仮想環境を作成し依存関係をインストール
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    poetry install

# アプリケーションをビルドするステージ
FROM python:3.11

# 環境変数を設定して仮想環境を有効にする
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係と仮想環境をコピー
COPY --from=requirements-stage /opt/venv /opt/venv
COPY . .

# コンテナ起動時に実行するコマンドを指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
