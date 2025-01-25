import os

class TokenManager:
    def __init__(self):
        # 環境変数から複数トークンを取得
        self.tokens = [
            os.getenv("LINE_CHANNEL_ACCESS_TOKEN"),
            os.getenv("LINE_CHANNEL_ACCESS_TOKEN2"),

        ]
        self.tokens = [token for token in self.tokens if token]  # 有効なトークンのみ
        self.current_token_index = 0

    def get_current_token(self):
        return self.tokens[self.current_token_index]

    def switch_token(self):
        self.current_token_index = (self.current_token_index + 1) % len(self.tokens)
        return self.get_current_token()