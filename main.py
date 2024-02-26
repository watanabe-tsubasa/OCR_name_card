from modules.line_handler import(
  handle_signature,
  events_handler
)

from dotenv import load_dotenv;load_dotenv()
from fastapi import Request, FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
favicon_path = './public/favicon.ico'

@app.get("/")
def read_root():
  return {"message": "bot server start"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
  return FileResponse(favicon_path)

@app.post("/callback")
async def handle_callback(request: Request):
  signature = request.headers['X-Line-Signature']
  body = await request.body()
  body = body.decode()

  events = handle_signature(body, signature)
  await events_handler(events)