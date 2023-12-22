import os
import httpx
import uvicorn
from fastapi import FastAPI, Request

from routers import webhook

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

client = httpx.AsyncClient()

app = FastAPI()
app.include_router(webhook.router)

@app.post("/webhook/")
async def webhook(req: Request):
    data = await req.json()
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    await client.get(f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}")

    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)