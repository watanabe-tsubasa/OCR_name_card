from modules.vision_api import detect_text
from modules.create_chat import create_chat
from modules.post_stein import post_stein_api
from dotenv import load_dotenv;load_dotenv()

if __name__ == '__main__':
  try: 
    res_text = detect_text('./data/test.jpg')
  except Exception as e:
    print(e)
  try:
    name_card_text = create_chat(res_text)
    res_gpt = name_card_text.choices[0].message.content
  except Exception as e:
    print(e)
  try:
    res = post_stein_api(res_gpt)
  except Exception as e:
    print(e)
    
  print(res)
  print(type(res))