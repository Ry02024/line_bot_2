import unittest
from services.line_bot import LineBot

class TestLineBot(unittest.TestCase):
    def setUp(self):
        # LineBotクラスのインスタンスを作成
        self.line_bot = LineBot()

    def test_line_bot_configuration(self):
        # LINE APIの設定が正しく完了することを確認
        try:
            self.line_bot._configure_line_bot()
            print("✅ LINE Messaging APIの設定が正常に完了しました。")
        except Exception as e:
            self.fail(f"❌ LINE Messaging APIの設定に失敗しました: {e}")

    def test_post_to_line(self):
        # テスト用メッセージをLINEに送信
        test_message = "テストメッセージ: LINE Bot動作確認"
        try:
            self.line_bot.post_to_line(test_message)
            print(f"✅ メッセージ送信成功: {test_message}")
        except Exception as e:
            self.fail(f"❌ メッセージ送信に失敗しました: {e}")
            
    def test_post_to_line_invalid_group_id(self):
        # 異常系: 不正なGroup ID
        invalid_group_id = "InvalidID"
        Config.LINE_GROUP_ID = invalid_group_id
        with self.assertRaises(ValueError):
            self.line_bot.post_to_line("テストメッセージ")
            
if __name__ == "__main__":
    unittest.main()
