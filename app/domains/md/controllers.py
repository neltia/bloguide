from fastapi import APIRouter
from app.domains.md.service import MarkdownService
# from app.domains.md.models import MarkdownFile
from app.common.response_model import ResponseResult

router = APIRouter()
service = MarkdownService()


# 검색 API 엔드포인트
@router.get("/search", response_model=ResponseResult)
async def test_api(query: str):
    return await service.search(query)
