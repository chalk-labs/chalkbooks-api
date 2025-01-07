
import os
from pathlib import Path

from pymongo import MongoClient
from config import *
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.core.config import settings
from app.api.main import api_router
import config

dotenv_file = Path(f".env.dev")
load_dotenv(dotenv_file)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return {"message": "Hello, World!"}


app.include_router(api_router, prefix=settings.API_V1_STR)
