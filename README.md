# line_bot_2

このプロジェクトは、Google Gemini AIを使用して生成された記事をLINEグループに自動投稿するLINE Botのアプリケーションです。Pythonで構築されており、モジュール化された構造で管理されています。

---

## ディレクトリ構造

以下のような構造でプロジェクトが構成されています：

```plaintext
project/
├── src/
│   ├── config.py           # 環境変数の管理
│   ├── gemini.py           # Gemini APIのロジック
│   ├── line_bot.py         # LINE Messaging APIのロジック
│   └── main.py             # メイン処理
└── requirements.txt        # 必要なライブラリ
```

---

## 必要条件

- Python 3.8以上
- 必要な環境変数（`.env`ファイルまたはシステムに設定）：
  - `LINE_CHANNEL_ACCESS_TOKEN`: LINE Messaging APIのアクセストークン
  - `LINE_GROUP_ID`: LINEグループID
  - `GEMINI_API_KEY`: Google Gemini APIのAPIキー

---

## セットアップ

1. **リポジトリをクローン**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **必要なライブラリをインストール**
   ```bash
   pip install -r requirements.txt
   ```

3. **環境変数の設定**
   `.env`ファイルまたはシステム環境変数に以下を設定します：
   ```plaintext
   LINE_CHANNEL_ACCESS_TOKEN=your_line_token
   LINE_GROUP_ID=your_line_group_id
   GEMINI_API_KEY=your_gemini_api_key
   ```

---

## 使用方法

1. **メインスクリプトの実行**
   ```bash
   python src/main.py
   ```

2. 実行後、以下の処理が行われます：
   - ランダムにトピックが選ばれます。
   - Gemini AIを使用して選択されたトピックに基づき記事が生成されます。
   - 生成された記事がLINEグループに投稿されます。

---

## モジュール説明

- **`config.py`**: 環境変数の読み取りと管理を担当します。
- **`gemini.py`**: Google Gemini APIのロジック（記事生成）を担当します。
- **`line_bot.py`**: LINE Messaging APIを使用してメッセージを送信します。
- **`main.py`**: 全体のフローを管理します。

---

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。

---

## 貢献

このプロジェクトへの貢献を歓迎します。バグ報告や新しい機能の提案については、[Issues](https://github.com/your-username/your-repository/issues)でご連絡ください。
```
