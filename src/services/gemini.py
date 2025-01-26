import google.generativeai as genai
from services.config import Config  # パスを修正

class Gemini:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self._configure_gemini()

    def _configure_gemini(self):
        genai.configure(api_key=self.api_key)
        print("✅ Gemini APIの設定が完了しました。")

    def generate_article(self, topic):
        prompt = f"""
        以下のトピックについて、100字以内で簡潔に丁寧語で説明してください。
        トピック: {topic}
        """
        try:
            response = genai.GenerativeModel(model_name="gemini-1.5-pro").generate_content(contents=[prompt])
            return response.text.strip() if response.text else "記事を生成できませんでした。"
        except Exception as e:
            print(f"❌ Gemini APIエラー: {e}")
            return "Gemini APIで記事生成に失敗しました。"
