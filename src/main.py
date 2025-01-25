import os
import random
from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
import google.generativeai as genai

# 環境変数からアクセストークンとグループIDを取得
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")  # LINEアクセストークン
group_id = os.getenv("LINE_GROUP_ID")  # LINEグループID
gemini_api_key = os.getenv("GEMINI_API_KEY")  # Gemini APIキー

# 必須環境変数の確認
if not channel_access_token or not group_id or not gemini_api_key:
    raise ValueError("必要な環境変数が設定されていません。")

# LINE Messaging APIクライアントの設定
configuration = Configuration(access_token=channel_access_token)
api_client = ApiClient(configuration=configuration)
messaging_api = MessagingApi(api_client=api_client)

# Gemini APIの設定
genai.configure(api_key=gemini_api_key)
print("✅ Gemini APIの設定が完了しました。")

# トピックリスト
TOPICS = [
    "食生活の工夫 - 健康的かつ簡単なレシピ。",
    "時間管理とリフレッシュ方法。",
    "趣味の探索 - 新しいスキルに挑戦。",
    "心地よい生活空間作り。",
    "運動と健康管理。",
    "言語学習の工夫。",
    "テクノロジーを活用した生活最適化。",
    "自己成長のための読書。",
    "家族や友人との時間の過ごし方。",
    "季節ごとの楽しみ方。",
]

# ランダムなトピックを選択
def select_random_topic():
    return random.choice(TOPICS)

# 記事を生成
def generate_article(topic):
    prompt = f"""
    以下のトピックについて、100字以内で簡潔に丁寧語で説明してください。
    トピック: {topic}
    """
    try:
        # Gemini APIで文章を生成
        response = genai.generate_text(model="text-bison-001", prompt=prompt)

        # レスポンスから生成された文章を取得
        if response and response.candidates:
            return response.candidates[0]["output"]  # 正しい属性でテキストを取得
        else:
            return "記事を生成できませんでした。"
    except Exception as e:
        print(f"❌ Gemini APIエラー: {e}")
        return "Gemini APIで記事生成に失敗しました。"

# LINEにメッセージを送信
def post_to_line(text):
    try:
        # メッセージを作成して送信
        message = TextMessage(text=text)
        push_message_request = PushMessageRequest(to=group_id, messages=[message])
        messaging_api.push_message(push_message_request)
        print(f"✅ メッセージ送信成功: {text}")
    except Exception as e:
        print(f"❌ LINEメッセージ送信エラー: {e}")

# メイン処理
if __name__ == "__main__":
    try:
        # トピックをランダムに選択
        topic = select_random_topic()
        print(f"✅ 選択されたトピック: {topic}")

        # Geminiで記事を生成
        article = generate_article(topic)
        print(f"✅ 生成された記事: {article}")

        # 記事をLINEに投稿
        message_content = article[:140]  # 140文字に制限
        print(f"✅ 投稿内容: {message_content}")

        post_to_line(message_content)
    except Exception as e:
        print(f"❌ エラー: {e}")
