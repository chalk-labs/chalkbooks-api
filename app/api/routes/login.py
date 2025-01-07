
import os
from fastapi import APIRouter, Body, HTTPException
from fastapi.security import OAuth2PasswordBearer

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
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import requests
import jwt
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests

router = APIRouter(tags=["login"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Replace these with your own values from the Google Developer Console
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")


@router.get('/login')
def get_login():
    return {"message": "Redirect to Google login"}

@router.get("/login/google")
async def login_google():
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    }


class TokenRequest(BaseModel):
    token: str

@router.post("/auth/google")
def verify_google_token(data: TokenRequest):
    try:
        # Verify the token with Google
        idinfo = id_token.verify_oauth2_token(
            data.token, requests.Request(), GOOGLE_CLIENT_ID
        )

        # Extract user information
        user_id = idinfo["sub"]
        email = idinfo["email"]
        name = idinfo.get("name", "User")

        # Here you can create a session or generate JWT
        return {"message": "User authenticated", "user_id": user_id, "email": email, "name": name}
    
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")



# @router.post("/save-transcript")
# async def connect_to_dailybots(payload: dict = Body(...)):
#     ConversationTranscript.create_from_(payload)
#     return payload