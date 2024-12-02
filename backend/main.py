from fastapi import FastAPI, Request
import openai

import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages", [])
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o",
        messages=messages
    )
    return response