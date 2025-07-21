from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import EllaChatbot

app = FastAPI()
bot = EllaChatbot()

# CORS setup for frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    bot_response = bot.chat(user_message)
    return {"response": bot_response}
