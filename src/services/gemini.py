import time
from google.api_core.exceptions import InternalServerError
import google.generativeai as genai
from services.config import Config  # パスを修正

class Gemini:
    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self._configure_gemini()

    def _configure_gemini(self):
        genai.configure(api_key=self.api_key)
        print("✅ Gemini APIの設定が完了しました。")

    def generate_article(self, topic, retries=3, delay=5):
        prompt = f"""
        以下のトピックについて、100字以内で簡潔に丁寧語で説明してください。
        トピック: {topic}
        """
        for attempt in range(retries):
            try:
                response = genai.GenerativeModel(model_name="gemini-1.5-pro").generate_content(contents=[prompt])
                if not response.text:
                    raise ValueError("Gemini APIで有効なレスポンスが得られませんでした。")
                return response.text.strip()
            except InternalServerError as e:
                print(f"❌ Gemini APIエラー (リトライ {attempt + 1}/{retries}): {e}")
                time.sleep(delay)  # 再試行前に一定時間待つ
                if attempt == retries - 1:
                    raise  # 最後の試行でも失敗したら例外をスロー
            except Exception as e:
                print(f"❌ その他のエラー: {e}")
                raise

