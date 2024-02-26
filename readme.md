# OCR_NAME_CARD

- 写真を撮って送るとスプレッドシートに登録してくれるLINE Botのソースです

## 実行環境

- Python 3.12.2
- venv
- その他`requirements.txt`に記載

## 構成

### サーバー `main.py`

- FastAPI

### OCR `vision_api.py`

- GCP cloud vision API
  - 認証するためのJSONはbase64エンコードして環境変数に設定

### 項目の分割 `create_chat.py`

- OPENAI API `gpt-4-turbo-preview` のJSONモードを利用

### データベース `post_stein.py`

- スプレッドシートを利用
- [Stein](https://steinhq.com/)を利用してAPI化
- APIエンドポイントは環境変数に設定

### LINE Bot `line_handler.py`

- LINE経由でのリクエストに対する処理を記述

### 環境変数

- GCP_JSON_STR
- LINE_CHANNEL_ACCESS_TOKEN
- LINE_CHANNEL_SECRET
- OPENAI_API_KEY
- STEIN_URL

### ホスティング先

- [Render](https://render.com/)

## その他ファイル

### `encoder.py`

- base64エンコード時に利用
