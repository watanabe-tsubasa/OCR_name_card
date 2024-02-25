import base64
import json

def decode_json(encoded_str: str) -> dict:
  # エンコードされた文字列をデコードしてバイト列に戻す
  decoded_bytes = base64.b64decode(encoded_str)

  # バイト列を文字列にデコード
  decoded_str = decoded_bytes.decode('utf-8')

  # 文字列をJSONオブジェクトに変換
  decoded_data = json.loads(decoded_str)

  return decoded_data

if __name__ == "__main__":
  import os
  from dotenv import load_dotenv; load_dotenv()

  encoded_str = os.getenv('GCP_JSON_STR')
  json = decode_json(encoded_str=encoded_str)
  print(json)
  print(type(json))