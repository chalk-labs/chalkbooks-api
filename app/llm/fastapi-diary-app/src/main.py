from fastapi import FastAPI
from routers.diary import router as diary_router

app = FastAPI()

app.include_router(diary_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Diary App!"}