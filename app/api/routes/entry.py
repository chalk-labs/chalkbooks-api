
from typing import List
from fastapi import APIRouter, Body, HTTPException
from app.llm_script import llm_json_maker
from model import User, Entry
router = APIRouter(tags=["entry"])


@router.get('/entry/create')
async def create_entry_from_request():
    user_id = "112259286812638363771"
    user = User.objects(id=user_id).first()
    entry = Entry(title="hello day", content="this is the first day", images=["https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&q=80&w=200"], mood="😊", date="12-12-2025", activities=["jogging", "watching videos", "planning build"], feelings=[
        {"emoji": "😊", "text": "motivated"},
        {"emoji": "✨", "text": "inspired"}
    ], user_id=user)
    entry.save()
    return {entry}


@router.get('/entry/user/{user_id}/date/{date}')
async def get_entry(user_id, date):
    # Implement logic to get entry from database
    print(f"reached here: {user_id}, {date}")
    user = User.objects(id=user_id).first()
    entry: Entry = Entry.objects(user_id=user, date=date).first()
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    return {
        "id": entry.id,
        "user_id": entry.user_id,
        "title": entry.title,
        "content": entry.content,
        "images": entry.images,
        "mood": entry.mood,
        "date": entry.date,
        "activities": entry.activities,
        "feelings": entry.feelings,
        "created_at": entry.created_at,
        "updated_at": entry.updated_at
    }


@router.get('/entry/user/{user_id}')
async def get_entries_by_user(user_id):
    # Implement logic to get entries from database
    print(f"reached here: {user_id}")
    user : User = User.objects(id=user_id).first()
    entries : List[Entry] = Entry.objects(user_id=user)
    if not entries:
        raise HTTPException(status_code=404, detail="entries not found")
    return [{
        "id": entry.id,
        "user_id": user.id,
        "title": entry.title,
        "content": entry.content,
        "images": entry.images,
        "mood": entry.mood,
        "date": entry.date,
        "activities": entry.activities,
        "feelings": entry.feelings,
        "created_at": entry.created_at,
        "updated_at": entry.updated_at
    } for entry in entries]


@router.post('/entry/new')
async def create_entry(data: dict = Body(...)):
    entry = Entry.create_from_(data)
    return entry.id

# update entry


@router.post('/entry/update')
async def update_entry(data: dict = Body(...)):
    entry = Entry.objects(id=data['id']).first()
    if not entry:
        raise HTTPException(status_code=404, detail="entry not found")
    entry.update(**data)
    return data

@router.post('/llm/newEntry')
async def create_entry_from_llm(data: dict = Body(...)):
    return llm_json_maker(data['text'])