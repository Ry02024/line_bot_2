from services.config import Config

if __name__ == "__main__":
    try:
        Config.validate()
        print("✅ 環境変数が正しく設定されています！")
        print(f"LINE_CHANNEL_ACCESS_TOKEN: {Config.LINE_CHANNEL_ACCESS_TOKEN}")
        print(f"LINE_GROUP_ID: {Config.LINE_GROUP_ID}")
        print(f"GEMINI_API_KEY: {Config.GEMINI_API_KEY}")
    except ValueError as e:
        print(f"❌ 環境変数のエラー: {e}")
