import requests
import json

# APIのエンドポイントとパラメータを指定
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/220000.json"


# APIからデータを取得
response = requests.get(url)

# レスポンスのJSONデータを解析
data = json.loads(response.text)

print(data)

# 降水量を抽出
precipitation = [0]

# 結果を表示
print(f"浜松市の降水確率: {precipitation}%")
