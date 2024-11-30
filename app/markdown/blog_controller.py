from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.get("/upload/list")
async def get_upload_list():
    return {"uploads": ["upload1", "upload2"]}


@router.post("/upload/md")
async def upload_markdown(file: UploadFile = File(...)):
    content = await file.read()
    # 마크다운 파일 업로드 로직 추가
    return {"filename": file.filename, "content": content}


@router.post("/upload/blog")
async def upload_blog(content: str):
    # 네이버 블로그 마크다운 변환 및 업로드 로직 추가
    return {"message": "Blog uploaded"}


@router.get("/list")
async def get_blog_list():
    return {"blogs": ["blog1", "blog2"]}


@router.post("/search")
async def search_blog(query: dict):
    # 엘라스틱서치 검색 로직 추가
    return {"results": ["result1", "result2"]}


@router.get("/{blog_id}")
async def get_blog(blog_id: str):
    return {"blog_id": blog_id, "content": "blog_content"}


@router.get("/{blog_id}/detail")
async def get_blog_detail(blog_id: str):
    return {"blog_id": blog_id, "content": "blog_content", "details": "blog_details"}


@router.get("/{blog_id}/download")
async def download_blog(blog_id: str):
    return {"blog_id": blog_id, "file": "markdown_file"}


@router.get("/{blog_id}/download/pdf")
async def download_blog_pdf(blog_id: str):
    return {"blog_id": blog_id, "file": "pdf_file"}


@router.get("/{blog_id}/download/html")
async def download_blog_html(blog_id: str):
    return {"blog_id": blog_id, "file": "html_file"}
