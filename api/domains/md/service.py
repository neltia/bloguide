from fastapi import HTTPException, status
from api.utils.es_utils import AsyncElasticsearchUtils
from api.common.response_model import ResponseResult
from api.common.result_helper import create_response

from datetime import datetime
from hashlib import sha256


class MarkdownService:
    def __init__(self):
        self.es = AsyncElasticsearchUtils()
        self.index = "blog_posts"

    """ 마크다운 생성 """
    async def create_markdown(self, post_data: dict):
        title = post_data["title"]
        content = post_data["content"]
        tags_manual = post_data["tags"]

        # 전처리 데이터 생성
        content_parsed = content
        metadata = await self.generate_metadata(content)

        # 저장할 데이터 구성
        markdown_data = {
            "title": title,
            "content_raw": content,
            "content_parsed": content_parsed,
            "tags": {"manual": tags_manual},
            "summary": metadata["summary"],
            "sentiment": metadata["sentiment"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "uploaded_by": "neltia",  # 디폴트 값
            "visibility": "public"   # 디폴트 값
        }

        # Elasticsearch에 저장
        response = await self.es.create_document(index=self.index, document=markdown_data)
        data = {"doc_id": response["_id"]}
        return create_response(result_code=status.HTTP_200_OK, data=data)

    # 콘텐츠 전처리 (예: Nori 분석 결과 결합)
    async def preprocess_content(self, content: str) -> str:
        tokens = await self.es.analyze_text(index=self.index, field="content_raw", text=content)
        return " ".join(tokens)

    # 콘텐츠를 기반으로 추가 메타데이터 생성
    async def generate_metadata(self, content: str) -> dict:
        content_hash = sha256(content.encode()).hexdigest()
        sentiment = "positive" if "좋은" in content else "neutral"  # <to-do> 감정 분석
        summary = content[:100]  # 첫 100자 추출
        return {"content_hash": content_hash, "sentiment": sentiment, "summary": summary}

    """ 마크다운 문서 데이터 조회 """
    async def get_markdown(self, doc_id: str) -> dict:
        response = await self.es.get_document(index=self.index, doc_id=doc_id)
        if response is None:
            return create_response(result_code=status.HTTP_404_NOT_FOUND)
        data = response["_source"]
        return create_response(result_code=status.HTTP_200_OK, data=data)

    """ 마크다운 문서 검색 """
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
        return create_response(result_code=status.HTTP_200_OK, data=mock_data)

    """ 마크다운 수정 """
    async def update_markdown(self, doc_id: str, update_data: dict) -> ResponseResult:
        if "content_raw" in update_data:
            update_data["content_parsed"] = await self.preprocess_content(update_data["content_raw"])
        return await self.es.update_document(index=self.index, doc_id=doc_id, update_data=update_data)

    """ 마크다운 삭제 """
    async def delete_markdown(self, doc_id: str) -> ResponseResult:
        response = await self.es.delete_document(index=self.index, doc_id=doc_id)
        if response is None:
            return create_response(result_code=status.HTTP_404_NOT_FOUND)
        data = response["result"]
        return create_response(result_code=status.HTTP_200_OK, data=data)
