import unittest
from services.config import TokenManager
from services.gemini import Gemini
from services.line_bot import LineBot

class TestMain(unittest.TestCase):
    def setUp(self):
        # デバッグ用に環境変数の確認
        self.token_manager = TokenManager()
        print(f"✅ 設定されたトークン: {self.token_manager.tokens}")

    def test_main_flow(self):
        # GeminiとLineBotの動作確認
        gemini = Gemini()
        line_bot = LineBot()
    
        topic = "テストトピック: 実行フロー確認"
        print(f"✅ {topic}")
    
        # 記事を生成
        article = gemini.generate_article(topic)
        self.assertIsNotNone(article, "Gemini APIで記事が生成されませんでした。")
        print(f"✅ 生成された記事: {article}")
    
        # 生成された記事が空でないことを確認
        if len(article.strip()) == 0:
            self.fail("❌ 生成された記事が空です。Gemini APIの動作を確認してください。")
    
        # メッセージを送信
        try:
            line_bot.post_to_line(article[:140])
            print("✅ メッセージ送信成功")
        except Exception as e:
            self.fail(f"❌ メッセージ送信失敗: {e}")


if __name__ == "__main__":
    unittest.main()
