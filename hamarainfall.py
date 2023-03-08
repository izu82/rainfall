import requests
from bs4 import BeautifulSoup

# 浜松市の降雨量のページのURL
url = 'https://tenki.jp/amedas/5/25/50456.html'

# リクエストを送信して、レスポンスを取得する
response = requests.get(url)

# レスポンスからHTMLを取得する
html = response.content

# BeautifulSoupオブジェクトを作成する
soup = BeautifulSoup(html, 'html.parser')

# 降水量の情報があるテーブルを取得する
table = soup.find_all("body")[0]


# テーブルの各行を取得する
rows = table.find_all("tr")


# 各行の情報を取得する
data = []
for row in rows:
    # 各行のセルを取得する
    cells = row.find_all("td")
    row_data = []
    for cell in cells:
        # もし、セル内に入れ子になった要素がある場合は、再帰的にその要素を探索する
        sub_elements = cell.find_all(recursive=False)
        if len(sub_elements) > 0:
            sub_data = []
            for sub_element in sub_elements:
                sub_data.append(sub_element.text.strip())
            row_data.append(sub_data)
        else:
            row_data.append(cell.text.strip())
    data.append(row_data)


print(data[3])
