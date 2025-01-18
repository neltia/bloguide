from fastapi import APIRouter
from api.domains.naver_blog.service import BlogParserService

router = APIRouter()
service = BlogParserService()
