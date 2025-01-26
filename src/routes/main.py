import random
import sys
import os
from src.services.config import Config
from src.services.gemini import Gemini
from src.services.line_bot import LineBot

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

def select_random_topic():
    return random.choice(TOPICS)

if __name__ == "__main__":
    try:
        # 環境変数を確認
        Config.validate()

        # トピックをランダムに選択
        topic = select_random_topic()
        print(f"✅ 選択されたトピック: {topic}")

        # Geminiで記事を生成
        gemini = Gemini()
        article = gemini.generate_article(topic)
        print(f"✅ 生成された記事: {article}")

        # 記事をLINEに投稿
        message_content = article[:140]  # 140文字に制限
        print(f"✅ 投稿内容: {message_content}")

        line_bot = LineBot()
        line_bot.post_to_line(message_content)
    except Exception as e:
        print(f"❌ エラー: {e}")
