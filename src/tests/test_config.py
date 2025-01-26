from services.config import Config, TokenManager

if __name__ == "__main__":
    try:
        # 環境変数を検証
        Config.validate()

        # トークン管理のテスト
        token_manager = TokenManager()
        print(f"✅ 現在のトークン: {token_manager.get_current_token()}")

        # トークンを切り替え
        token_manager.switch_token()
        print(f"✅ 切り替え後のトークン: {token_manager.get_current_token()}")

        # 再切り替え
        token_manager.switch_token()
        print(f"✅ 再切り替え後のトークン: {token_manager.get_current_token()}")
    except ValueError as e:
        print(f"❌ エラー: {e}")
