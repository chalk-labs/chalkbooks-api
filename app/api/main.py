from fastapi import APIRouter

from app.api.routes import login, user, entry

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(user.router)
api_router.include_router(entry.router)


# if settings.ENVIRONMENT == "local":
#     api_router.include_router(private.router)