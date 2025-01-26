import unittest
from services.gemini import Gemini

class TestGemini(unittest.TestCase):
    def setUp(self):
        # Geminiクラスのインスタンスを作成
        self.gemini = Gemini()

    def test_generate_article(self):
        # 有効なトピックを使用して記事が生成されることを確認
        topic = "テストトピック - Gemini動作確認"
        try:
            article = self.gemini.generate_article(topic)
            self.assertTrue(len(article) > 0, "記事が生成されていません。")
            print(f"✅ 生成された記事: {article}")
        except Exception as e:
            self.fail(f"❌ Gemini APIで記事生成中にエラーが発生しました: {e}")

if __name__ == "__main__":
    unittest.main()
