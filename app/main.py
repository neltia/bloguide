from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from app.core.config import settings
from app.api.routers import api_router
from app.common.error_handler_custom import generic_exception_handler, http_exception_handler

import time
import logging


# app instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# templates
templates = Jinja2Templates(directory="app/templates")

# static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Custom Error handler
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


# middleware: API 요청 시간 로깅
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.perf_counter()  # 요청 시작 시간
    response = await call_next(request)  # 다음 처리로 넘어감
    end_time = time.perf_counter()  # 요청 종료 시간

    process_time = end_time - start_time
    logger.info(f"Request: {request.method} {request.url} completed in {process_time:.4f} seconds")
    return response


# Include API routers
app.include_router(api_router, prefix=settings.API_PREFIX)


# root url request
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": settings.PROJECT_NAME}
    )


# DB Connection init
@app.on_event("startup")
async def startup_event():
    print("Application started")


# DB Connectoin close
@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutting down")
