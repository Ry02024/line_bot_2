import unittest
from services.gemini import Gemini

class TestGemini(unittest.TestCase):
    def setUp(self):
        # Geminiクラスのインスタンスを作成
        self.gemini = Gemini()

    def test_gemini_configuration(self):
        # APIキーが正しく設定されることを確認
        try:
            self.gemini._configure_gemini()
            print("✅ Gemini APIの設定が正常に完了しました。")
        except Exception as e:
            self.fail(f"❌ Gemini APIの設定に失敗しました: {e}")

    def test_generate_article(self):
        # 有効なトピックを使用して記事が生成されることを確認
        topic = "テストトピック - Gemini動作確認"
        article = self.gemini.generate_article(topic)
        self.assertTrue(len(article) > 0, "記事が生成されていません。")
        print(f"✅ 生成された記事: {article}")

if __name__ == "__main__":
    unittest.main()
