from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest
from services.config import Config, TokenManager

class LineBot:
    def __init__(self):
        self.token_manager = TokenManager()
        self.group_id = Config.LINE_GROUP_ID  # グループIDをインスタンス変数に保存
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
                
                # デバッグログ
                print(f"📤 送信リクエスト: Group ID: {Config.LINE_GROUP_ID}, Text: {text}")
                self.messaging_api.push_message(push_message_request)
                print(f"✅ メッセージ送信成功: {text}")
                return
    
            except Exception as e:
                # 無効な `to` フィールドのエラーを特定して ValueError を発生
                if "The property, 'to', in the request body is invalid" in str(e):
                    raise ValueError(f"無効なGroup IDが指定されています: {Config.LINE_GROUP_ID}")
                
                print(f"⚠️ メッセージ送信エラー: {e}")
                self.token_manager.switch_token()
        
        # 全てのトークンで失敗した場合
        raise RuntimeError("全てのトークンでメッセージ送信に失敗しました。")

