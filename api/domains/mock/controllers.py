from fastapi import APIRouter
from api.domains.mock.service import BoardSearvice
from api.common.response_model import ResponseResult

router = APIRouter()
service = BoardSearvice()


# 검색 API 엔드포인트 (테스트)
@router.get("/search", response_model=ResponseResult)
async def test_api(query: str):
    return await service.search(query)
