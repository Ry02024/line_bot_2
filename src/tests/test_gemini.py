import unittest
from services.gemini import Gemini

class TestGemini(unittest.TestCase):
    def setUp(self):
        self.gemini = Gemini()

    def test_gemini_configuration(self):
        # Gemini APIの設定が完了することを確認
        try:
            self.gemini._configure_gemini()
            print("✅ Gemini APIの設定が完了しました。")
        except Exception as e:
            self.fail(f"❌ Gemini APIの設定に失敗しました: {e}")

    def test_generate_article(self):
        # 有効なトピックで記事が生成されることを確認
        topic = "テストトピック - 機能の検証"
        article = self.gemini.generate_article(topic)
        self.assertTrue(len(article) > 0, "記事が生成されていません。")
        print(f"✅ 生成された記事: {article}")

    def test_generate_article_error(self):
        # エラーが発生した場合に適切なメッセージが返ることを確認
        self.gemini.api_key = None  # 無効なAPIキーを設定
        article = self.gemini.generate_article("無効なトピック")
        self.assertEqual(article, "Gemini APIで記事生成に失敗しました。")
        print("✅ エラーハンドリングが正しく動作しました。")

if __name__ == "__main__":
    unittest.main()
