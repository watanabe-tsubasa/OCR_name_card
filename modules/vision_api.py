from modules.decode_json import decode_json
import os
from dotenv import load_dotenv; load_dotenv()

def detect_text(path: str = None, content: bytes=None):
  encoded_str = os.getenv('GCP_JSON_STR')
  dict_data = decode_json(encoded_str=encoded_str)
  
  """Detects text in the file."""
  from google.cloud import vision
  from google.oauth2 import service_account
  
  credentials = service_account.Credentials.from_service_account_info(dict_data)

  client = vision.ImageAnnotatorClient(credentials=credentials)
  
  if path is not None:
    with open(path, "rb") as image_file:
      content = image_file.read()

  image = vision.Image(content=content)

  response = client.text_detection(image=image)
  texts = response.text_annotations
  text = texts[0].description
  
  # text_list = []
  # for text in texts:
  #   text_list.append(text.description)
    # print(f'\n"{text.description}"')

    # vertices = [
    #   f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
    # ]

    # print("bounds: {}".format(",".join(vertices)))

  if response.error.message:
    raise Exception(
      "{}\nFor more info on error messages, check: "
      "https://cloud.google.com/apis/design/errors".format(response.error.message)
    )
      
  return text

if __name__ == "__main__":
  res_text = detect_text('./data/test.jpg')
  print(res_text)