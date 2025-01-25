import os

class Config:
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    LINE_GROUP_ID = os.getenv("LINE_GROUP_ID")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
