from fastapi import APIRouter
from app.frontend.md.controllers import router as posts_router

front_router = APIRouter()

# markdown View, Analyzer API
front_router.include_router(posts_router, prefix="/posts")
