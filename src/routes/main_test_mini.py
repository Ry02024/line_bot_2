import os
import requests

# 環境変数を取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN2")
GROUP_ID = os.getenv("LINE_GROUP_ID")

# 取得した `groupId` を確認する
print(f"📌 DEBUG: GROUP_ID = '{GROUP_ID}'")  # GitHub Actions のログに出力

# `groupId` が None や空ならエラーを出す
if not GROUP_ID or not GROUP_ID.startswith("C"):
    raise ValueError("❌ ERROR: 環境変数 `LINE_GROUP_ID` が正しく設定されていません！")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
}

data = {
    "to": GROUP_ID.strip(),  # スペース・改行削除
    "messages": [
        {"type": "text", "text": "GitHub Actions からのテストメッセージ"}
    ]
}

# API リクエストを送信
response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)

# レスポンスのステータスと内容をログに出力
print(f"📌 DEBUG: Response Status Code = {response.status_code}")
print(f"📌 DEBUG: Response JSON = {response.json()}")

def send_message():
    """LINEグループに「あ」を送る関数"""
    if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_GROUP_ID:
        raise ValueError("環境変数が設定されていません。GitHub Secretsを確認してください。")

    # LINE APIの設定
    config = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
    api_client = ApiClient(configuration=config)
    messaging_api = MessagingApi(api_client=api_client)

    # 送信するメッセージ
    message = TextMessage(text="あ")
    request = PushMessageRequest(to=LINE_GROUP_ID, messages=[message])

    # メッセージ送信
    messaging_api.push_message(request)
    print("メッセージを送信しました: あ")

if __name__ == "__main__":
    send_message()
