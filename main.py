
import os
import requests
from fastapi import FastAPI, Request, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from pathlib import Path
from typing import Optional
from pprint import pprint
from config import *
from fastapi.middleware.cors import CORSMiddleware
from model import ConversationTranscript
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/save-transcript")
async def connect_to_dailybots(payload: dict = Body(...)):
    ConversationTranscript.create_from_(payload)
    return payload