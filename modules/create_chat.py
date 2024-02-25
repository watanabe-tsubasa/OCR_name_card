from openai import OpenAI
from dotenv import load_dotenv;load_dotenv()

def create_chat(string: str) -> str:

  client = OpenAI()
  schema = {
    "会社名": "string",
    "部署名": "string",
    "氏名": "string",
    "会社住所": "string | null",
    "電話番号": "string | null",
    "e-mailアドレス": "string | null",
  }

  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": f"次の文字列から会社名、部署名、氏名、会社住所、電話番号、e-mailアドレスを抜き出して、JSON形式で出力してください。JSONのスキーマは次の通りです：{schema}"},
      {"role": "user", "content": string}
    ]
  )

  return response

if __name__ == '__main__' :
  response = create_chat("\n\nAEON イオンリテール株式会社\n木を植えています\n私たちはイオンです\nEC本部\nEC戦略部 ISF構築グループ\nわた\n渡邊\nつばさ\n翼\nSOM FORE\nISO\n14001\nJAC\nNACH DENGAN\nOCHIFFICATO\nEC00J0033\n〒261-0023 千葉県千葉市美浜区中瀬14\nE-mail:watanabe-tsuba@aeonpeople.biz\n再生紙を使用しております\nMS\nJAB\nCM021")
  print(response.choices[0].message.content)
