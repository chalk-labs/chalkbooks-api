
from fastapi import APIRouter, Body, HTTPException
from model import User, Entry
router = APIRouter(tags=["entry"])



# class Entry(me.Document):
    # id = me.StringField(primary_key=True)
    # user_id = me.ReferenceField(User)
    # title = me.StringField()
    # content = me.StringField()
    # image = me.URLField()
    # mood = me.StringField()
    # date = me.DateTimeField()
    # activities = me.ListField(me.StringField())
    # feelings = me.ListField(me.StringField())
    # created_at = me.DateTimeField(auto_now_add=True)
    # updated_at = me.DateTimeField(auto_now=True)
    
@router.get('/entry/create')
async def create_entry_from_request():
    user_id = "112259286812638363771"
    user = User.objects(id=user_id).first()
    entry = Entry(title="hello day", content="this is the first day", image="https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&q=80&w=200", mood="😊", date="12-12-2025", activities=["jogging", "watching videos", "planning build"], feelings=[
        { "emoji": "😊", "text": "motivated" },
        { "emoji": "✨", "text": "inspired" }
      ], user_id=user)
    entry.save()
    return { entry}


@router.get('/entry/user/{user_id}/date/{date}')
async def get_entry(user_id, date):
    # Implement logic to get entry from database
    print(f"reached here: {user_id}, {date}")
    user = User.objects(id=user_id).first()
    entry = Entry.objects(user_id=user, date=date).first()
    if entry is None:
        raise HTTPException(status_code=404, detail="entry not found")
    return {"title": entry.title, "date": entry.date, "content": entry.content, "user_id": user.id}

@router.get('/entry/user/{user_id}')
async def get_entries_by_user(user_id):
    # Implement logic to get entries from database
    print(f"reached here: {user_id}")
    user = User.objects(id=user_id).first()
    entries = Entry.objects(user_id=user)
    if not entries:
        raise HTTPException(status_code=404, detail="entries not found")
    return [{"title": entry.title, "date": entry.date, "content": entry.content, "user_id": user.id} for entry in entries]

@router.post('/entry/new')
async def create_entry(data: dict = Body(...)):
    entry = Entry.create_from_(data)
    return entry.id

#update entry
@router.post('/entry/update')
async def update_entry(data: dict = Body(...)):
    entry = Entry.objects(id=data['id']).first()
    if not entry:
        raise HTTPException(status_code=404, detail="entry not found")
    entry.update(**data)
    return data

@router.post('/entry/login')
async def login_entry(data: dict = Body(...)):
    entry = Entry.objects(id=data['id']).first()
    if entry:
        return entry
    entry.create_from_(data)
    return data



# @router.post("/save-transcript")
# async def connect_to_dailybots(payload: dict = Body(...)):
#     ConversationTranscript.create_from_(payload)
#     return payload