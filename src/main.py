import os
import random
from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
import google.generativeai as genai

# 環境変数の取得
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_GROUP_ID or not GEMINI_API_KEY:
    raise ValueError("必要な環境変数が設定されていません。")

# Geminiの設定
def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    print("✅ Gemini APIの設定が完了しました。")

configure_gemini(GEMINI_API_KEY)

# トピックリスト
TOPICS = [
    "食生活の工夫 - 健康的かつ簡単なレシピ。",
    "時間管理とリフレッシュ方法。",
    "趣味の探索 - 新しいスキルに挑戦。",
    "心地よい生活空間作り。",
    "運動と健康管理。",
]

# ランダムなトピックを選択
def select_random_topic():
    return random.choice(TOPICS)

# 記事を生成
def generate_article(topic):
    prompt = f"以下のトピックについて100字以内で簡潔に説明してください: {topic}"
    response = genai.GenerativeModel(model_name="gemini-1.5-pro").generate_content(contents=[prompt])
    return response.text.strip() if response.text else "記事を生成できませんでした。"

# LINEにメッセージを送信
def post_to_line(text):
    try:
        configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
        api_client = ApiClient(configuration=configuration)
        messaging_api = MessagingApi(api_client=api_client)
        message = TextMessage(text=text)
        push_message_request = PushMessageRequest(to=LINE_GROUP_ID, messages=[message])
        messaging_api.push_message(push_message_request)
        print(f"✅ メッセージ送信成功: {text}")
    except Exception as e:
        print(f"❌ メッセージ送信失敗: {e}")

# メイン処理
if __name__ == "__main__":
    topic = select_random_topic()
    print(f"✅ 選択されたトピック: {topic}")

    article = generate_article(topic)
    print(f"✅ 生成された記事: {article}")

    post_to_line(article[:140])  # 140文字以内に制限
