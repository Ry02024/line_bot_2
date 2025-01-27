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
                # トークンを使用して設定を再構成
                self.access_token = self.token_manager.get_current_token()
                configuration = Configuration(access_token=self.access_token)
                self.api_client = ApiClient(configuration=configuration)
                self.messaging_api = MessagingApi(api_client=self.api_client)
    
                # メッセージを送信
                message = TextMessage(text=text)
                push_message_request = PushMessageRequest(to=Config.LINE_GROUP_ID, messages=[message])
                
                # デバッグ用ログ: 送信内容を表示
                print("📤 送信リクエスト内容:")
                print(f"Group ID: {Config.LINE_GROUP_ID}, Text: {text}")

                self.messaging_api.push_message(push_message_request)  # 実際の送信処理
                print(f"✅ メッセージ送信成功: {text}")
                return  # 成功したら終了

            except Exception as e:
                # エラー時にレスポンス詳細をログ出力
                print(f"⚠️ メッセージ送信エラー: {e}")
                
                # エラーがAPIクライアントによるものの場合、レスポンスの詳細を取得
                if hasattr(e, 'status') and hasattr(e, 'reason'):
                    print(f"レスポンスステータス: {e.status}")
                    print(f"レスポンス内容: {e.reason}")
                
                print("次のトークンを試します...")
                self.token_manager.switch_token()
        
        # 全てのトークンで失敗した場合、例外をスロー
        raise RuntimeError("全てのトークンでメッセージ送信に失敗しました。")
