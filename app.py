from modules.vision_api import detect_text
from modules.create_chat import create_chat

from dotenv import load_dotenv;load_dotenv()

if __name__ == '__main__':
  res_text = detect_text('./data/test.jpg')
  name_card_text = create_chat(res_text)
  print(name_card_text.choices[0].message.content)