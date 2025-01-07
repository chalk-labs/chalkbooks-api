# FILE: /fastapi-diary-app/fastapi-diary-app/src/routers/__init__.py
from fastapi import APIRouter

router = APIRouter()

from .diary import *  # Import all endpoints from diary.py