import os
import requests
from dotenv import load_dotenv; load_dotenv()

stein_url = os.getenv('STEIN_URL')

def post_stein_api(data: str):
  response = requests.post(
    stein_url,
    data=f'[{data}]',
    headers={"Content-Type": "application/json"},
  )
  
  if not response.ok:
    raise Exception(f"HTTP Error: {response.status_code} - {response.reason}")
  
  return response


if __name__ == '__main__':
  import json
  
  test_json = {
    "会社名": "イオンリテール株式会社",
    "部署名": "EC本部 EC戦略部 ISF構築グループ",
    "氏名": "渡邊 翼",
    "会社住所": "〒261-0023 千葉県千葉市美浜区中瀬14",
    "電話番号": "043-212-6133",
    "e-mailアドレス": "watanabe-tsuba@aeonpeople.biz"
  }
  test_json_str = json.dumps(test_json)
  res = post_stein_api(test_json_str)
  print(res.text)
  print(res.status_code)