from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
from config import Config

class LineBot:
    def __init__(self):
        self.access_token = Config.LINE_CHANNEL_ACCESS_TOKEN
        self.group_id = Config.LINE_GROUP_ID
        self._configure_line_bot()

    def _configure_line_bot(self):
        configuration = Configuration(access_token=self.access_token)
        self.api_client = ApiClient(configuration=configuration)
        self.messaging_api = MessagingApi(api_client=self.api_client)

    def post_to_line(self, text):
        try:
            message = TextMessage(text=text)
            push_message_request = PushMessageRequest(to=self.group_id, messages=[message])
            self.messaging_api.push_message(push_message_request)
            print(f"✅ メッセージ送信成功: {text}")
        except Exception as e:
            print(f"❌ LINEメッセージ送信エラー: {e}")
