import os

class Config:
    LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    @staticmethod
    def validate():
        """環境変数が正しく設定されているかを検証"""
        if not Config.LINE_GROUP_ID:
            raise ValueError("環境変数 LINE_GROUP_ID が設定されていません。")
        if not Config.GEMINI_API_KEY:
            raise ValueError("環境変数 GEMINI_API_KEY が設定されていません。")
        print("✅ 環境変数が正しく設定されています。")

class TokenManager:
    def __init__(self):
        """環境変数からLINEのトークンを動的に取得"""
        self.tokens = [
            value for key, value in os.environ.items()
            if key.startswith("LINE_CHANNEL_ACCESS_TOKEN") and value
        ]

        if not self.tokens:  # トークンが空の場合エラー
            raise ValueError("有効なトークンが設定されていません。環境変数を確認してください。")

        self.current_token_index = 0
        print(f"✅ {len(self.tokens)}個のトークンが設定されています。")

    def get_current_token(self):
        """現在のトークンを取得"""
        return self.tokens[self.current_token_index]

    def switch_token(self):
        """次のトークンに切り替え"""
        self.current_token_index = (self.current_token_index + 1) % len(self.tokens)
        print(f"✅ トークンを切り替えました: インデックス {self.current_token_index}")
        return self.get_current_token()
