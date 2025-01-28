import os
from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest

# 環境変数の取得（GitHub Secretsで設定）
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN2")
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID").strip()  # 余計な空白・改行を削除

print(f"GROUP_ID: {GROUP_ID}")  # これで groupId の出力を確認

if not GROUP_ID.startswith("C"):
    raise ValueError("GROUP_ID がグループIDの形式ではありません！")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
}

data = {
    "to": GROUP_ID,  # ここが正しく設定されているか
    "messages": [
        {"type": "text", "text": "GitHub Actions からのテストメッセージ"}
    ]
}

response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=data)
print(response.status_code, response.json())

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
