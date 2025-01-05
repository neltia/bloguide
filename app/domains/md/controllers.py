from fastapi import APIRouter
from app.domains.md.service import MarkdownService
# from app.domains.md.models import MarkdownFile
from app.common.response_model import ResponseResult
from app.infrastructure.db.get_conn import get_elasticsearch_client

router = APIRouter()
service = MarkdownService()


# Close Elasticsearch on application shutdown
@router.on_event("startup")
async def startup_event():
    await get_elasticsearch_client().ping()


# Close Elasticsearch on application shutdown
@router.on_event("shutdown")
async def shutdown_event():
    await get_elasticsearch_client().close()


# get markdown data
@router.post("/{post_id}", response_model=ResponseResult)
async def get_post_doc(post_id: str):
    return await service.get_markdown(post_id)


# 검색 API 엔드포인트
@router.get("/search", response_model=ResponseResult)
async def test_api(query: str):
    return await service.search(query)


# delete markdown data
@router.delete("/{post_id}", response_model=ResponseResult)
async def delete_post_doc(post_id: str):
    return await service.delete_markdown(post_id)
