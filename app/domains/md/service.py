from fastapi import HTTPException, status
from app.common.response_model import ResponseResult
from app.common.result_helper import create_response


class MarkdownService:
    async def search(self, query: str) -> ResponseResult:
        # 검색 로직 구현 (예: 데이터베이스, Elasticsearch 호출 등)
        if query.lower() == "error":
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Simulated error for testing")

        # Mock 데이터 반환
        mock_data = {
            "list": [
                {"title": "검색 결과 1", "link": "https://example.com/1"},
                {"title": "검색 결과 2", "link": "https://example.com/2"},
            ]
        }
        print(mock_data)
        return create_response(result_code=status.HTTP_200_OK, data=mock_data)
