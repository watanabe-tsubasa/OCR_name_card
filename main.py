import os
import sys

from dotenv import load_dotenv;load_dotenv()
from fastapi import Request, FastAPI, HTTPException

from linebot.v3.webhook import WebhookParser
from linebot.v3.messaging import (
  AsyncApiClient,
  AsyncMessagingApi,
  Configuration,
  ReplyMessageRequest,
  TextMessage
)
from linebot.v3.exceptions import (
  InvalidSignatureError
)
from linebot.v3.webhooks import (
  MessageEvent,
  TextMessageContent
)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
  print('Specify LINE_CHANNEL_SECRET as environment variable.')
  sys.exit(1)
if channel_access_token is None:
  print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
  sys.exit(1)

configuration = Configuration(
  access_token=channel_access_token
)

app = FastAPI()
async_api_client = AsyncApiClient(configuration)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(channel_secret)


@app.post("/callback")
async def handle_callback(request: Request):
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = await request.body()
  body = body.decode()

  try:
    events = parser.parse(body, signature)
  except InvalidSignatureError:
    raise HTTPException(status_code=400, detail="Invalid signature")

  for event in events:
    if not isinstance(event, MessageEvent):
      continue
    if not isinstance(event.message, TextMessageContent):
      continue

    await line_bot_api.reply_message(
      ReplyMessageRequest(
        reply_token=event.reply_token,
        messages=[TextMessage(text=event.message.text)]
      )
    )

  return 'OK'