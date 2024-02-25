import json
import base64

file_path = './divine-fuze-387415-8b3c994487be.json'

# JSONオブジェクト
with open (file_path, "r") as file:
  data = json.load(file)
# JSONオブジェクトを文字列に変換
json_str = json.dumps(data)

# 文字列をバイト列に変換してBase64エンコード
encoded_bytes = base64.b64encode(json_str.encode('utf-8'))

# エンコードされたバイト列を文字列に変換
encoded_str = encoded_bytes.decode('utf-8')

print("エンコードされたBase64文字列:")
print(encoded_str)
