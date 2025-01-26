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
            if not response.text:
                raise ValueError("Gemini APIで有効なレスポンスが得られませんでした。")
            return response.text.strip()
        except Exception as e:
            print(f"❌ Gemini APIエラー: {e}")
            raise  # 例外を再スローして処理を停止
