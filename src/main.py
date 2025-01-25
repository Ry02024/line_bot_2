from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

# 環境変数からアクセストークンとグループIDを取得
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
group_id = os.getenv("LINE_GROUP_ID")

def generate_message_with_gemini():
    """
    Geminiを使用して文章を生成する（仮の例として直接文章を返す）
    実際にはGeminiのAPIやインターフェースを呼び出して文章を取得
    """
    # Geminiから生成された文章を取得するロジックをここに実装
    # 仮にGeminiが「今日の天気は晴れです！」と生成したと仮定
    generated_message = "Geminiが生成したメッセージです: 今日の天気は晴れです！"
    return generated_message

def send_message():
    # LINE APIインスタンス作成
    line_bot_api = LineBotApi(channel_access_token)
    
    # Geminiで生成したメッセージを取得
    message_text = generate_message_with_gemini()
    
    # メッセージを送信
    message = TextSendMessage(text=message_text)
    line_bot_api.push_message(group_id, message)
    print("メッセージ送信完了")

if __name__ == "__main__":
    send_message()
