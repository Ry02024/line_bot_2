from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
from utils import TokenManager

class LineBot:
    def __init__(self):
        self.token_manager = TokenManager()
        self._configure_line_bot()

    def _configure_line_bot(self):
        self.access_token = self.token_manager.get_current_token()
        configuration = Configuration(access_token=self.access_token)
        self.api_client = ApiClient(configuration=configuration)
        self.messaging_api = MessagingApi(api_client=self.api_client)

    def post_to_line(self, text):
        for _ in range(len(self.token_manager.tokens)):  # トークンの数だけ試す
            try:
                self.access_token = self.token_manager.get_current_token()
                configuration = Configuration(access_token=self.access_token)
                self.api_client = ApiClient(configuration=configuration)
                self.messaging_api = MessagingApi(api_client=self.api_client)

                # メッセージを送信
                message = TextMessage(text=text)
                push_message_request = PushMessageRequest(to=Config.LINE_GROUP_ID, messages=[message])
                self.messaging_api.push_message(push_message_request)
                print(f"✅ メッセージ送信成功: {text}")
                return  # 成功したら終了
            except Exception as e:
                print(f"⚠️ エラー: {e}. 次のトークンを試します...")
                self.token_manager.switch_token()
        print("❌ 全てのトークンでメッセージ送信に失敗しました。")
