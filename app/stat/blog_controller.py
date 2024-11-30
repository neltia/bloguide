from fastapi import APIRouter

router = APIRouter()


@router.get("/{blog_id}")
async def get_blog_statistics(blog_id: str):
    return {"blog_id": blog_id, "statistics": "statistics_content"}


@router.post("/{blog_id}/download/excel")
async def download_blog_statistics_excel(blog_id: str):
    return {"blog_id": blog_id, "file": "statistics_excel_file"}
