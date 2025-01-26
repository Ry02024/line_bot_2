import os

class TokenManager:
    def __init__(self):
        # "LINE_CHANNEL_ACCESS_TOKEN" で始まるすべての環境変数を取得
        self.tokens = [
            value for key, value in os.environ.items()
            if key.startswith("LINE_CHANNEL_ACCESS_TOKEN") and value
        ]
        if not self.tokens:
            raise ValueError("有効なトークンが設定されていません。")

        self.current_token_index = 0

    def get_current_token(self):
        return self.tokens[self.current_token_index]

    def switch_token(self):
        self.current_token_index = (self.current_token_index + 1) % len(self.tokens)
        return self.get_current_token()
