from fastapi import APIRouter, Body
from services.openai_service import process_transcript

router = APIRouter(tags=["diary"])

@router.post("/diary/summarize")
async def summarize_day(transcript: dict = Body(...)):
    summary = await process_transcript(transcript["text"], task="summarize")
    return {"summary": summary}

@router.post("/diary/title")
async def generate_title(transcript: dict = Body(...)):
    title_with_emoji = await process_transcript(transcript["text"], task="generate_title")
    return {"title": title_with_emoji}

@router.post("/diary/mood")
async def analyze_mood(transcript: dict = Body(...)):
    mood_analysis = await process_transcript(transcript["text"], task="mood_analysis")
    return {"mood": mood_analysis}

@router.post("/diary/activities")
async def list_activities(transcript: dict = Body(...)):
    activities = await process_transcript(transcript["text"], task="list_activities")
    return {"activities": activities}

@router.post("/diary/reflections")
async def provide_reflections(transcript: dict = Body(...)):
    reflections = await process_transcript(transcript["text"], task="provide_reflections")
    return {"reflections": reflections}