import unittest
from services.gemini import Gemini
from services.line_bot import LineBot

class TestMain(unittest.TestCase):
    def test_main_flow(self):
        gemini = Gemini()
        line_bot = LineBot()

        # テスト用トピック
        topic = "テストトピック: 実行フロー確認"
        print(f"✅ テスト用トピック: {topic}")

        # 記事を生成
        article = gemini.generate_article(topic)
        self.assertIsNotNone(article)
        print(f"✅ 生成された記事: {article}")

        # メッセージを送信
        try:
            line_bot.post_to_line(article[:140])  # 140文字に制限
            print("✅ メッセージ送信成功")
        except Exception as e:
            self.fail(f"❌ メッセージ送信失敗: {e}")

if __name__ == "__main__":
    unittest.main()
