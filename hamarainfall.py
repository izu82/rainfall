import requests
from bs4 import BeautifulSoup

# 浜松市のページのURL
url = 'https://www.jma.go.jp/bosai/amedas/#area_type=offices&area_code=220000&amdno=50331&format=table1h&elems=53614'

# リクエストを送信して、レスポンスを取得する
response = requests.get(url)

# レスポンスからHTMLを取得する
html = response.content

# BeautifulSoupオブジェクトを作成する
soup = BeautifulSoup(html, 'html.parser')

# 降水量の情報があるテーブルを取得する
table = soup.find_all(id="amd-table")

print(table)
