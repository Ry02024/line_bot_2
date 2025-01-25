from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# 環境変数からアクセストークンとグループIDを取得
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
group_id = os.getenv("LINE_GROUP_ID")

def send_message():
    # LINE APIインスタンス作成
    line_bot_api = LineBotApi(channel_access_token)
    
    # メッセージを送信
    message = TextSendMessage(text="おはようございます！LINE Botからの自動メッセージです。")
    line_bot_api.push_message(group_id, message)
    print("メッセージ送信完了")

if __name__ == "__main__":
    send_message()
