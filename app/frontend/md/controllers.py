from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates/posts")


# markdown view
@router.get("/view")
async def root(request: Request):
    return templates.TemplateResponse("view.html", {"request": request})
