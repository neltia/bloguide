from typing import Any, Optional
from api.infrastructure.db.get_conn import get_elasticsearch_client
from elasticsearch.exceptions import NotFoundError

es_client = get_elasticsearch_client()


class AsyncElasticsearchUtils:
    def __init__(self):
        self.client = es_client

    # Elasticsearch 문서 생성
    async def create_document(self, index: str, document: dict) -> Any:
        return await self.client.index(index=index, body=document)

    # Elasticsearch 문서 조회
    async def get_document(self, index: str, doc_id: str) -> Optional[dict]:
        try:
            return await self.client.get(index=index, id=doc_id)
        except NotFoundError:
            return None

    # Elasticsearch 문서 수정
    async def update_document(self, index: str, doc_id: str, update_data: dict) -> Any:
        try:
            return await self.client.update(index=index, id=doc_id, body={"doc": update_data})
        except NotFoundError:
            return None

    # Elasticsearch 문서 삭제
    async def delete_document(self, index: str, doc_id: str) -> Any:
        try:
            return await self.client.delete(index=index, id=doc_id)
        except NotFoundError:
            return None

    # Elasticsearch 문서 검색
    async def search_documents(self, index: str, query: dict) -> list:
        response = await self.client.search(index=index, body=query)
        return response

    # Elasticsearch _analyze API 호출
    async def analyze_text(self, index: str, field: str, text: str) -> list:
        payload = {"field": field, "text": text}
        response = await self.client.indices.analyze(index=index, body=payload)
        return [token["token"] for token in response["tokens"]]
