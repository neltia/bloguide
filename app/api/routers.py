from fastapi import APIRouter
from app.domains.mock.controllers import router as mock_router
from app.domains.md.controllers import router as markdown_router

api_router = APIRouter()

# local test용 API
api_router.include_router(mock_router, prefix="/mock", tags=["Mock"])

# markdown View, Analyzer API
api_router.include_router(markdown_router, prefix="/markdown", tags=["Markdown"])
