# 依存関係をインストールするステージ
FROM python:3.11 as requirements-stage

# 作業ディレクトリを設定
WORKDIR /tmp

# Poetryをインストール
RUN pip install poetry

# 依存関係ファイルをコピー
COPY pyproject.toml* poetry.lock* /tmp/

# 依存関係をエクスポート
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# アプリケーションをビルドするステージ
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# アプリケーションのコードをコピー
COPY . /app

# コンテナ起動時に実行するコマンドを指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
