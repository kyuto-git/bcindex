import csv
import requests

print("Script started")

# CSVファイルからリンクを読み取る
with open('updated_links.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # ヘッダー行をスキップ
    next(reader)
    links = [row[0] for row in reader]

# ダウンロード先のディレクトリを指定
save_directory = "./downloaded_files/"

for link in links:
    try:
        # リンクからファイルをダウンロード
        response = requests.get(link, timeout=10)
        response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
        # ダウンロードしたファイルを保存
        with open(save_directory + link.split('/')[-1], 'wb') as file:
            file.write(response.content)
    except requests.RequestException as e:
        # エラーが発生した場合、エラーメッセージを表示して次のリンクに進む
        print(f"Error downloading {link}: {e}")
