ターミナル（またはコマンドプロンプト）を開き、Dockerfileとdownload_script.pyが保存されているディレクトリに移動します。次に、以下のコマンドを実行してDockerイメージをビルドします：

docker build -t python_downloader .


このコマンドは、現在のディレクトリにあるDockerfileを使用して、python_downloaderという名前のDockerイメージをビルドします。



ホストOS上で、ダウンロードしたファイルを保存するディレクトリを指定してコンテナを起動します：

docker run -v ~/Desktop/docker-python/downloaded_files:/app/downloaded_files python_downloader


このコマンドは、ホストOSの ~/Desktop/docker-python/downloaded_files ディレクトリを、コンテナ内の /app/downloaded_files ディレクトリにマウントします。これにより、download_script.py によってダウンロードされたファイルは、ホストOSの指定のディレクトリに直接保存されます。



--------------------


. コンテナのログの確認
コンテナのログを確認して、スクリプトの実行中にエラーやその他のメッセージが出力されていないかを確認します。コンテナのIDや名前が必要です。これは docker ps -a コマンドで一覧表示されます。


docker logs [コンテナIDまたはコンテナ名]

このコマンドで表示されるログにエラーメッセージやダウンロードの進捗情報などが表示されます。