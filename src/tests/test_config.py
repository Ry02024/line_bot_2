from services.config import Config, TokenManager

if __name__ == "__main__":
    try:
        Config.validate()
        token_manager = TokenManager()
        print(f"✅ 現在のトークン: {token_manager.get_current_token()}")

        token_manager.switch_token()
        print(f"✅ 切り替え後のトークン: {token_manager.get_current_token()}")

        token_manager.switch_token()
        print(f"✅ 再切り替え後のトークン: {token_manager.get_current_token()}")
    except ValueError as e:
        print(f"❌ エラー: {e}")
