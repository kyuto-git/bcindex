# ARMアーキテクチャ向けのPythonの公式イメージをベースとして使用
FROM python:3.9-slim-buster

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストール
RUN pip install requests

# イメージ内に downloaded_files ディレクトリを作成
RUN mkdir downloaded_files

# PythonスクリプトとCSVファイルをコンテナにコピー
COPY download_script.py .
COPY *.csv .

# スクリプトの実行コマンド
CMD ["python", "./download_script.py"]
