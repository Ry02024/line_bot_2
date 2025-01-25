from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
import os

# 環境変数からトークンとグループIDを取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")

# LINE Messaging APIの設定
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
api_client = ApiClient(configuration=configuration)
messaging_api = MessagingApi(api_client=api_client)

def send_message_to_group():
    try:
        # 送信するメッセージ
        message = TextMessage(text="おはようございます！今日はどんな一日になるでしょうか？")
        
        # LINEグループに送信
        push_message_request = PushMessageRequest(to=LINE_GROUP_ID, messages=[message])
        messaging_api.push_message(push_message_request)
        print("✅ メッセージ送信成功")
    except Exception as e:
        print(f"❌ メッセージ送信失敗: {e}")

if __name__ == "__main__":
    send_message_to_group()
