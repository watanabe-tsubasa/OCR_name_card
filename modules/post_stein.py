import json
import os
import requests
from dotenv import load_dotenv; load_dotenv()

stein_url = os.getenv('STEIN_URL')

def post_stein_api(data: dict):
  data_str = json.dumps(data)
  response = requests.post(
    stein_url,
    data=f'[{data_str}]',
    headers={"Content-Type": "application/json"},
  )
  
  if not response.ok:
    raise Exception(f"HTTP Error: {response.status_code} - {response.reason}")
  
  return response

if __name__ == '__main__':
  
  test_json = {
    "会社名": "test株式会社",
    "部署名": "test本部 test戦略部 test構築グループ",
    "氏名": "test man",
    "会社住所": "",
    "電話番号": "",
    "e-mailアドレス": "test@test.jp"
  }

  res = post_stein_api(test_json)
  print(res.text)
  print(res.status_code)