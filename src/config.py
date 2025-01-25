import os

class Config:
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    @staticmethod
    def validate():
        if not Config.LINE_CHANNEL_ACCESS_TOKEN:
            raise ValueError("環境変数 LINE_CHANNEL_ACCESS_TOKEN が設定されていません。")
        if not Config.LINE_GROUP_ID:
            raise ValueError("環境変数 LINE_GROUP_ID が設定されていません。")
        if not Config.GEMINI_API_KEY:
            raise ValueError("環境変数 GEMINI_API_KEY が設定されていません。")
