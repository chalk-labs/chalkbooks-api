
from fastapi import APIRouter, Body, HTTPException
from model import User
router = APIRouter(tags=["user"])

    
@router.get("/user/hi")
def hello():
    return {"message": "Hello, User"}

@router.get('/user/create')
async def create_user_from_request():
    user = User(name="Alice", email="alice@example.com", id = "124532")
    user.save()
    return {"id": str(user.id), "name": user.name, "email": user.email}


@router.get('/user/{id}')
async def get_user(id: int):
    # Implement logic to get user from database
    print(f"reached here: {id}")

    user = User.objects(id=id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

@router.post('/user/new')
async def create_user(data: dict = Body(...)):
    user = User.objects(id=data['id']).first()
    if user:
        raise HTTPException(status_code=409, detail="User already exists")
    User.create_from_(data)
    return data

@router.post('/user/login')
async def login_user(data: dict = Body(...)):
    user = User.objects(id=data['id']).first()
    if user:
        return user
    User.create_from_(data)
    return data



# @router.post("/save-transcript")
# async def connect_to_dailybots(payload: dict = Body(...)):
#     ConversationTranscript.create_from_(payload)
#     return payload