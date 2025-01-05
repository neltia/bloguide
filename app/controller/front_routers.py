from fastapi import APIRouter
from app.frontend.md.controllers import router as posts_router

front_router = APIRouter(include_in_schema=False)

# markdown View, Analyzer API
front_router.include_router(posts_router, prefix="/posts")
